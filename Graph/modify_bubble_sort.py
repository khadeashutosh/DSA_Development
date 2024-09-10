def modify_bubble_sort(data_list):
  flag=False
  for r in range(1,len(data_list)):
    flag=False
    for c in range(len(data_list)-r):
      if data_list[c]>data_list[c+1]:
        data_list[c],data_list[c+1]=data_list[c+1],data_list[c]
        flag=True
    if not flag:
      break  

result=[100000,20,3000,40,50,600,700,8,900,100]
modify_bubble_sort(result)
print(result)                 