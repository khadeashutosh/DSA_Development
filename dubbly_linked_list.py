class Node:
  def __init__(self,prev=None,item=None,next=None) :
    self.prev=prev
    self.item=item
    self.next=next
    
class Dll:
  def __init__(self,start=None):
    self.start=start
    
  def is_empty(self):
    return self.start==None 
  
  def insert_at_start(self,data):
    n=None(None,data,self.start)
    if not self.is_empty():
      self.start.prev=n
    self.start=n 
    
  def insert_at_last(self,data):
    temp=self.start
    if self.start !=None:
      while temp.next !=None:
        temp=temp.next
    n=Node(temp,data,None)
    if temp==None:
      self.start=n
    else:
      temp.next=n  
      
  def search(self,data):
        temp=self.start
        while temp != None:
          if temp.item==data:
            return temp
          temp=temp.next
        return None
      
  def insert_after(self,temp,data):      
    if temp is not None:
      n=Node(temp,data,temp.next)
      if temp.next is not None:
        temp.next.prev=n
      temp.next=n
        
            