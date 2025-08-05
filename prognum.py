def fibonatchi(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonatchi(n - 1) + fibonatchi(n - 2)