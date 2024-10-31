def sum_n_odd(n):
  if n==1:
    return 1
  return (2*n-1+sum_n_odd(n-1))
print(sum_n_odd(10))