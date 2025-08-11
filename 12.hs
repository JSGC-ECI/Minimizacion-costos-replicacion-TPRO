minimizarCosto c = dp !! n
  where
    n = length c
    dp = [minCosto i | i <- [0..n]]

    minCosto i
      | i == 0 = 0
      | otherwise = minimum [dp !! (j - 1) + c !! (j - 1) + costoAcceso j i | j <- [1..i]]

    costoAcceso :: Int -> Int -> Int
    costoAcceso j i = (i - j) * (i - j + 1) `div` 2
