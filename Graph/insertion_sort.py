def insertion_sort(list1):
  for i in range(1,len(list1)):
    temp=list1[i]
    j=i-1
    while j>=0 and temp<list1[j]:
      list1[j+1]=list1[j]
      j-=1
    list1[j+1]=temp
mylist=[122,4,6,88,97,56,45,35,75,24,58,555]
insertion_sort(mylist)
print(mylist)