module NGrams (NGram(..), ngrams) where

import Data.List (splitAt)

data NGram a = NGram Int [a] deriving (Show)

getNG :: Int -> [a] -> [a]
getNG n = fst . splitAt n

makeNG :: Int -> a -> [a] -> NGram a
makeNG n pad xs = NGram n $ take n (xs ++ (repeat pad))

ngrams :: Int -> a -> [a] -> [NGram a]
ngrams n pad xs = ngs xs []
                where ngs [] acc = reverse acc
                      ngs ts acc = ngs (tail ts) ((makeNG n pad (getNG n ts)):acc)
