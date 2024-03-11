class Queqe:
  def __init__(self):
    self.item=[]
    
  def is_empty(self):
    return len(self.item)==0
  
  def enqueqe(self,data):
    self.item.append(data)
    
  def dequeqe(self):
    if not self.is_empty():
      self.item.pop(0)
    else:
      raise IndexError ("Queqe is Empty")
    
  def get_front(self):
    if not self.is_empty():
      return self.item[0]
    
    else:
      raise IndexError ("Queqe is Empty")
      
  def get_rare(self)  :
    if not self.is_empty():
      return self.item[-1]
    else:
      raise IndexError ("Queqe is Empty")
      
  def size(self):    
    return len(self.item)
  
q1=Queqe()  
try:
  q1.get_front()
except Exception as e:
  print(e.args[0],"please insert some value here")  
q1.enqueqe(10)
q1.enqueqe(20)
q1.enqueqe(30)
q1.enqueqe(40)

print(q1.get_front(),"= value is  Fronted means oldest value")
print(q1.get_rare()," = value is rared latest value") 
print(q1.size(),"Queqe has now")
print()
try:
  q1.dequeqe()
  print("Queqe has now", q1.size(), "Element")        
except Exception as e:
  print(e.args())