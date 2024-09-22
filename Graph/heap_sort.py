class Heap_sort:
  def __init__(self):
    self.heap=[]

  def create_heap(self,list1): 
    for e in list1:
      self.insert(e) 

  def insert(self,e):
    index=len(self.heap)
    parent_index=(index-1)//2
    while index>0 and self.heap[parent_index]<e:
      if index==len(self.heap):
        self.heap.append(self.heap[parent_index]) 
      else:
        self.heap[index]=self.heap[parent_index]
      index=parent_index
      parent_index=(index-1)//2
    if index==len(self.heap):
      self.heap.append(e)
    else:
      self.heap[index]=e

  def top(self):
    if len(self.heap)==0:
      raise EmptyHeapException()
    return self.heap[0]
  
  def delete(self):
    if len(self.heap)==0:
      raise EmptyHeapException()
    if len(self.heap)==1:
      return self.heap.pop()
    max_value=self.heap[0]
    temp=self.heap.pop()
    index=0
    leftChildIndex=2*index+1
    rightChildIndex=2*index+2

    while leftChildIndex<len(self.heap):
      if rightChildIndex<len(self.heap):
        if self.heap[leftChildIndex]>self.heap[rightChildIndex]:
          if self.heap[leftChildIndex]>temp:
            self.heap[index]=self.heap[leftChildIndex]
            index=leftChildIndex
          else:
            break  
        else:
          if self.heap[rightChildIndex]>temp:
            self.heap[index]=self.heap[rightChildIndex]
            index=rightChildIndex
          else:
            break

      else: #no right child
        if self.heap[leftChildIndex]>temp:
          self.heap[index]=self.heap[leftChildIndex]
          index=leftChildIndex
        else:
          break        
      
      leftChildIndex=2*index+1
      rightChildIndex=2*index+2
    self.heap[index]=temp
    return max_value

  def heap_sort(self,list1):
    self.create_heap(list1)
    list2=[]
    try:
      while True:
        list2.insert(0,self.delete())
    except EmptyHeapException:
      pass    
    return list2
class EmptyHeapException(Exception):
  def __init__ (self,msg="Empty Heap"):
    self.msg=msg

  def __str__(self) :
    return self.msg
    
list1=[12,45,65,98,34,23,41,2,67,5,10]
h=Heap_sort()
list1=h.heap_sort(list1)
print(list1)  