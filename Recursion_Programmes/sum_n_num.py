def n_sum(n):
  if n==1:
    return 1
  return n+n_sum(n-1)
    
result=n_sum(10)    
print(result)
  