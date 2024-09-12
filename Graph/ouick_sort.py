def quick_sort(list1):
  if len(list1)<=1:
    return list1
  else:
    pivot=list1[0]
    lesser=[x for x in list1[1:] if x<=pivot]
    gretter=[x for x in list1[1:] if x>pivot]
    return quick_sort(lesser)+[pivot]+quick_sort(gretter)


mylist=[22,56,77,88,24,45,34,99,46,70]
mylist=quick_sort(mylist)
print(mylist)