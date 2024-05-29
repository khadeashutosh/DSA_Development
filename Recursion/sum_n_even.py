def sum_n_even(n):
  if n==1 :
    return 2
  return (2*n +sum_n_even(n-1))
print(sum_n_even(10))