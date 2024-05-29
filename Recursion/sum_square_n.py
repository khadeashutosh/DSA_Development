def n_squre(n):
  if n==0:
    return 1
  return n*n + n_squre(n-1)
print("square is ", n_squre(10)) 