def odd_number(n):
  if n>0:
    print(2*n-1,end=' ')
    odd_number(n-1)    
odd_number(10)   