f :: Int -> [Int] -> [Int]
f n = foldr (\x acc -> if n > x then x : acc else acc) []

-- The Input/Output section. You do not need to change or modify this part
main = do
  n <- readLn :: IO Int
  inputdata <- getContents
  let numbers = map read (lines inputdata) :: [Int]
  putStrLn . unlines $ (map show . f n) numbers