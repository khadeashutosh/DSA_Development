
def odd_number(n):
  if n>0:
    odd_number(n-1)
    print(2*n-1,end=' ')
odd_number(10)  