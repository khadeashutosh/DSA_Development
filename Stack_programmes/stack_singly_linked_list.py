class Node:
  def __init__(self,item=None , next=None):
    self.item=item
    self.next=next
class Stack:
  def __init__(self):
    self.top=None
    self.item_count=0
  def is_empty(self):
    return self.top==None
  
  def push(self,data): 
    new_node=Node(data, self.top)
    self.top=new_node
    self.item_count+=1
    
  def pop(self):
    if not self.is_empty():
      data=self.top.item
      self.top=self.top.next
      self.item_count-=1
      return data
    else:
     raise IndexError ("Stack is empty")    
  def peek(self):
    if not self.is_empty():
      return self.top.item
    else:
      raise IndexError ("Stack is empty")
    
  def size(self):
    return self.item_count
  
s1=Stack()
s1.push(10) 
s1.push(20)
s1.push(30)
s1.push(40)
print("Total element in the stack",s1.size())
print("Total element on the stack",s1.peek())
print("delete element is" ,s1.pop())
print("Now Total element in the stack",s1.size())