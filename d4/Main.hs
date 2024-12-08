import Data.List (transpose)

main :: IO ()
main =  readFile "input.txt" >>= \con -> print $ countXmases ( lines con)

countXmases :: [String] -> Int
countXmases s = sum [ countXmasesHorizontally s
                    , (countXmasesHorizontally . reverse) s
                    , countXmasesVertically s
                    , (countXmasesVertically . reverse ) s
                    , countXmasesDiagonally s
                    , (countXmasesDiagonally . reverse) s
                    , countXmasesReverseDiagonally s
                    , (countXmasesReverseDiagonally . reverse) s
                    ]
                
countXmasesOnLine :: Int -> String ->  Int
countXmasesOnLine sum h@('X' : 'M' : 'A' : 'S' : xs) = countXmasesOnLine (sum+1) (tail h) 
-- countXmasesOnLine sum h@('S' : 'A' : 'M' : 'X' : xs) = countXmasesOnLine (sum+1) (tail h)
countXmasesOnLine sum [] = sum
countXmasesOnLine sum xs = countXmasesOnLine sum (tail xs)
 
countXmasesHorizontally :: [String] -> Int
countXmasesHorizontally xs = sum $ map (countXmasesOnLine 0) xs 

countXmasesVertically :: [String] -> Int
countXmasesVertically xs = countXmasesHorizontally (transpose xs)

