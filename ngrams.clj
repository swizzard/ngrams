(ns ngrams)

(defn ngrams
  [n pad tokens] (partition n 1 (repeat pad) tokens))
