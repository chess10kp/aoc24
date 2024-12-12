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

countXmasesDiagonally :: [String] -> Int
countXmasesDiagonally xs = countXmasesHorizontally $ diagonals xs

countXmasesReverseDiagonally :: [String] -> Int
countXmasesReverseDiagonally xs = countXmasesHorizontally $ reverseDiagonals xs
                               

diagonals :: [String] -> [String]
diagonals grid = [ [grid !! (i + k) !! k | k <- [0 .. min (m - i - 1) (n - 1)]] | i <- [0 .. m - 1]] ++
                 [ [grid !! k !! (j + k) | k <- [0 .. min (m - 1) (n - j - 1)]] | j <- [1 .. n - 1]]
  where
    m = length grid
    n = if null grid then 0 else length (head grid)

reverseDiagonals :: [String] -> [String]
reverseDiagonals xs = map reverse $ diagonals xs 
