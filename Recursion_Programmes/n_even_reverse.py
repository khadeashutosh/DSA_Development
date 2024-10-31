
def even_number(n):
  if n>0:
    print(2*n-2,end=' ')
    even_number(n-1)
   
even_number(10)      