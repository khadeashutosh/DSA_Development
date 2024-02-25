from singly_linked_list import*
class Stack:
  def __init__(self):
    self.mylist=Sll()
    self.item_count=0
  def is_empty(self):
    return self.mylist.is_empty()
  def push(self,data):
    self.mylist.insert_at_start(data)
    self.item_count+=1
  def pop(self):
    if not self.is_empty():
      self.mylist.delete_first()  
      self.item_count-=1
  def peek(self):
    if not self.is_empty()    :
      return self.mylist.item
  def size(self):
    return self.item_count
  
s1=Stack()    
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("This is the top  Element",s1.peek())
      
