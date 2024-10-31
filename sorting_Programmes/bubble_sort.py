def bubble_sort(data_list):
  for r in range(1,len(data_list)):
    for c in range(len(data_list)-r):
      if data_list[c]>data_list[c+1]:
        data_list[c],data_list[c+1]=data_list[c+1],data_list[c]

result=[100000,20,3000,40,50,600,700,8,900,100]
bubble_sort(result)
print(result)