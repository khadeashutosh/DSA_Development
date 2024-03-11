class Node:
  def __init__(self,item=None, next=None):
    self.item=item
    self.next=next
class Queqe:
  def __init__(self):
    self.front=None
    self.rare=None
    self.item_count=0
    
  def is_empty(self):
    return self.item_count==0   
  
  def enqueqe (self,data):
    n=Node(data)
    if self.is_empty():
      self.front=n
    else:
      self.rare.next=n
    self.rare=n   
    self.item_count+=1
    
  def dequeqe(self):  
    if self.is_empty():
      raise IndexError ("Queqe is not empty")
    
    elif self.front== self.rare:
      self.front=None     #here is one node
      self.rare=None
      
    else:  #Here is more than one node
      self.front=self.front.next
    self.item_count-=1
    
    
  def get_front(self)      :
    if self.is_empty():
      raise IndexError ("Queqe is not empty")
    else:
      return self.front.item
    
  def get_rare(self):
    if self.is_empty():
      raise IndexError("Queqe is not empty")
    else:
      return self.rare.item
    
  def size (self):
    return self.item_count
  
  
q1=Queqe()
q1.enqueqe(10)      
q1.enqueqe(20)
q1.enqueqe(30)
q1.enqueqe(40)
print("This is the oldest value",q1.get_front())
print("This is the latest value",q1.get_rare())
print("current values are",q1.size())
q1.dequeqe()
print("after deletion the values are",q1.size())
    
      