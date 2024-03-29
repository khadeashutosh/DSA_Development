from singly_linked_list import*
class Stack(Sll):
  def __init__(self):
    super(). __init__()
    self.count_item=0
  def is_empty(self):
    return super().is_empty()
  
  def push(self,data):
    self.insert_at_start(data)
    self.count_item+=1
  
  def pop(self):
    if not self.is_empty():
      self.delete_first()
      self.count_item-=1
    else:
      raise IndentationError ("Stack is empty")  
  def peek(self):
    if not self.is_empty():
      return self.start.item
    else:
      raise IndexError ("Stack is empty")      
    
  def size(self):  
    return self.count_item

s1=Stack()    
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("Top element is ", s1.peek())
s1.pop()
print("Top element is ", s1.peek()) 