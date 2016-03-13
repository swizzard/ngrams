package main
import "fmt"

type Padding struct {
    padLeft, padRight interface{}
}

var DefaultPad Padding = Padding{nil, nil}

func Ngrams(n int, xs []interface{}, padding Padding) [][]interface{} {
    var i, j, c int
    var out [][]interface{}
    c = len(xs)
    out = make([][]interface{}, 0, c)
    i = 0
    if padding.padLeft != nil {
        j = 1
    } else {
        j = n
    }
    for {
        if i == c {
            return out
        }
        if j >= c {
            diff := n - (c - i)
            slc := xs[i:]
            for x := 0; x < diff; x++ {
                slc = append(slc, padding.padRight)
            }
            out = append(out, slc)
        } else {
            if ldiff := n - j; ldiff > 0 {
                if padding.padLeft != nil {
                    slc := make([]interface{}, 0, n)
                    for x := 0; x < ldiff; x++ {
                        slc = append(slc, padding.padLeft)
                    }
                    slc = append(slc, xs[i:j]...)
                    out = append(out, slc)
                    i--
                } else {
                    out = append(out, xs[i:j])
                }
            } else {
                out = append(out, xs[i:j])
            }
        }
    i++
    j++
    }
}


func main() {
    xs := make([]interface{}, 10, 10)
    for i := 0; i < 10; i++ {
        xs[i] = i
    }
    fmt.Println("trigrams:\n\t", Ngrams(3, xs, DefaultPad))
    lpad := Padding{-1, nil}
    fmt.Println(Ngrams(3, xs, lpad))
}
