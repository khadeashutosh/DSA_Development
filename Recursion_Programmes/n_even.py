print("even number is printed")
print()
def even_number(n):
  if n>0:
    even_number(n-1)
    print(2*n-2,end=' ')
even_number(10)    