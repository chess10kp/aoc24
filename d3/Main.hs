main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ parseWholeString 0 True contents

parseWholeString :: Int -> Bool -> String -> Int
parseWholeString sum b [] = sum
parseWholeString sum b ('d':'o':'(':')':xs) = parseWholeString sum True xs
parseWholeString sum False (x:xs) = parseWholeString sum False xs
parseWholeString sum b ('d':'o' : 'n' : '\'' : 't':'(':')':xs) = parseWholeString sum False xs
parseWholeString sum True ('m':'u':'l':'(':xs) = readMuls sum 0 xs
parseWholeString sum b (x:xs) = parseWholeString sum b xs

readMuls :: Int -> Int -> String -> Int
readMuls sum 0 (x:xs) = case reads (x:xs) :: [(Int, String)] of
                                 [(n, (',': ys))] -> readMuls sum n (ys)
                                 [(_, xs)] -> parseWholeString (sum) True  xs

readMuls sum localSum (x:xs) = case reads (x:xs) :: [(Int, String)] of
                                 [(n, (')': ys))] -> parseWholeString (sum + localSum * n) True (ys)
                                 [(_, xs)] -> parseWholeString sum True xs
