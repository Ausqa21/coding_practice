f :: [Int] -> [Int]
f lst =
  let pairs = zip lst [0 .. length lst - 1]
      f1 = filter (\(a, b) -> odd b) pairs
   in map fst f1

main = do
  inputdata <- getContents
  mapM_ (putStrLn . show) . f . map read . lines $ inputdata