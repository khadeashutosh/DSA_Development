class Node:
  def __init__(self,item=None,next=None):
    self.item=item
    self.next=next
    
class Cll:
  def __init__(self,last=None):
    self.last=last
  
  def is_empty(self):
    return self.last ==None
  
  def insert_at_start(self,data):
    n=Node(data)
    if self.is_empty():
      n.next=n
      self.last=n
    else:
      n.next=self.last.next
      self.last.next=n
      
  def insert_at_last(self,data):
    n=Node(data)
    if self.is_empty():
      self.last=n
    else:
      n.next=self.last.next
      self.last.next=n
      self.last=n
  def search(self,data)    :
    if self.is_empty():
      return None
    temp=self.last.next
    while temp != self.last:
      if temp.item==data:
        return temp
      temp=temp.next
    if temp.item==data:
      return temp
    return None
  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(data,temp.next)  
      temp.next=n
      if temp ==self.last:
        self.last=n 
  
  def print_list(self):
    if not self.is_empty():
      temp=self.last.next
      while temp!= self.last:
        print(temp.item, end='  ')
        temp=temp.next
        print(temp.item)
  def delete_first(self):
    if not self.is_empty():
      if self.last.next==self.last:
        self.last=None
      else:
        self.last.next=self.last.next.next
  def delete_last(self):
    if not self.is_empty(self):
      if self.last.next==self.last:
        self.last=None
      else:
        temp=self.last.next
        while temp.next!=self.last:
          temp=temp.next
        temp.mext=self.last.next
        self.last=temp
  def delete_item(self,data):
    if not self.is_empty():
      if self.last.next==self.last:
        if self.last.item==data:
          self.last=None
      else:
        if self.last.next.item==data:
          self.delete_first()
        else:  
          temp=self.last.next
          while temp!=self.last:
            if temp.next==self.last:
              self.delete_last() 
              break
            if temp.next.item==data:
              temp.next=temp.next.next
              break
            temp=temp.next
  def __iter__(self):
    if self.last==None:
      return CllIterator(None)
    else:
      return CllIterator(self.last.next)
class CllIterator:
  def __init__(self,last):
    self.current=last
    self.last=last
    self.count=0
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current==None:
      raise StopIteration
    if self.current==self.last and self.count==1:
      raise StopIteration
    else:
      self.count=1
    data=self.current.item
    self.current=self.current.next
    return data                
mylist=Cll()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(40),50)
mylist.delete_first()
mylist.insert_after(mylist.search(10),20)
mylist.delete_item(30)
for x in mylist:
  print(x, end='  ')
print()
        
       
    
    