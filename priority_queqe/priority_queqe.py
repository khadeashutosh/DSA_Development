class PriorityQueqe:
  def __init__(self):
    self.items=[]
    
  def is_empty(self):
    return len(self.items)==0  
    
  def push(self,data,priority):
    index=0
    while index<len(self.items) and self.items[index][1]<=priority:
      index+=1
    self.items.insert(index,(data,priority))  
  
  def pop(self):
    if self.is_empty():
      raise IndexError ("Priority Queqe is empty")   
    return self.items.pop(0)[0]
    
  def size (self):
    return len(self.items)    

P1=PriorityQueqe()      
P1.push("Ashu",1)
P1.push(2,2)
P1.push("Mona",3)
P1.push(4,2)
print("Priority Queqe size is",P1.size()) 
while not P1.is_empty():
  print(P1.pop())
 