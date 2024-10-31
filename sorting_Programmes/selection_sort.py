def selection_sort(list1):
  no=len(list1)
  for i in range(no):
    min_index=i
    for j in range(i+1,no):
      if list1[j]<list1[min_index]:
        min_index=j
    list1[i],list1[min_index]=list1[min_index],list1[i]
li=[22,44,75,85,34,78,234,96,56]
selection_sort(li)
print(li)        

