class Node():
  def __init__(self,item=None,prev=None,next=None):
    self.prev=prev
    self.item=item
    self.next=next
    
class Deque:
  def __init__(self):
    self.front=None
    self.rare=None
    self.item_count=0
    
  def is_empty(self):
    return self.front==None
  
  def insert_front(self,data):
    n=Node(data)
    n.next=self.front
    n.prev=None  
    if self.is_empty():
      self.rare=n
    else:
       self.front.prev=n
    self.front=n
    self.item_count+=1
  
  def insert_rare(self,data):
    n=Node(data,self.rare,None)
    if self.is_empty():
      self.front=n
    else:
      self.rare.next=n  
    self.rare=n  
    self.item_count-=1
    
  def delete_front(self):
    if self.is_empty():
      raise IndexError ("Deque is empty")
    if self.front == self.rare:
      self.front==None
      self.rare==None 
    else:
      self.front=self.front.next
      self.front.prev=None
    self.item_count+=1
           
  def delete_rare(self):
    if self.is_empty():
      raise IndexError ("Deque is empty")
    
    if self.front==self.rare:
      self.front=None
      self.rare=None
    else:
      self.rare=self.rare.prev
      self.rare.next=None           
    self.insert_front-=1
  
  def get_front(self):
    if self.is_empty():
      raise IndexError ("Deque is empty")
    return self.front.item
  def get_rare(self):
    if self.is_empty():
      raise IndexError ("Deque is empty")
    return self.rare.item
  def size(self):
    return self.item_count
  
D1=Deque()
D1.insert_front(10)
D1.insert_front(20)   
D1.insert_rare(30)
D1.insert_rare(40)   
print("This is the oldest value of front",D1.get_front())
print("This is the latest value of front",D1.get_rare())

   
        