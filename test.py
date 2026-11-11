def combi(n, r):
  p = 1
  for i in range(1, r+1):
    p = p * (n - i + 1) // i
    return p

for n in range(0, 6):
  result = ''
  for r in range(0, n+1):
      result += '{:d}C{:d}={:<4d}'.format(n, r, combi(n, r))
      print(result)
