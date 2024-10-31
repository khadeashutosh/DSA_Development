class Deque:
  def __init__(self):
    self.items=[]
  
  def is_empty(self):
    return len(self.items)==0  
  def insert_front(self,data):
    self.items.insert(0,data)
    
  def insert_rare(self,data):
    self.items.append(data)
    
  def delete_front(self):
    try:
      if self.is_empty():
        print("Deque is not empty")
      else:
        self.items.pop(0)
    except Exception as e :
      print("this is indexerror ")
                
  def delete_rare(self):
    if self.is_empty():
      raise IndexError ("Deque is not empty")
    else:
      self.items.pop()    
      
  def get_front(self):
    if self.is_empty():
      raise IndexError("Deque is empty")
    else:
      return self.items[0]
     
  
  def get_rare(self):
    if self.is_empty():
      raise IndexError("Deque is empty")
    else:
      return self.items[-1] 
  def size(self):
    return len(self.items)  
  
D1=Deque()
D1.insert_front(10)
D1.insert_front(20)  
D1.insert_front(50)  

D1.insert_rare(30) 
D1.insert_rare(40)
D1.insert_rare(60) 
 


print("This is the oldest value (front)",D1.get_front())  
print("This is the latest value (rare)",D1.get_rare()) 
print("the values",D1.size())              
             
D1.delete_front()             
D1.delete_rare()
print("After Deletion The values area",D1.size())
