class Node:
  def __init__(self,item=None,prev=None,next=None):
    self.item=item
    self.prev=prev
    self.next=next
class Cdll:
  def __init__(self,start):    
    self.last=start
   
  def is_empty(self,data)  :
    return  self.start==None
  
  def insert_at_start(self,data): # creat method first
    n=Node(data)  #creat a new node and put none in it
    if self.is_empty(): #check it's empty or not
      n.next=n   #if empty it will one node then put his reference in it
      n.prev=n   #same in preve as well 
    else:   #if not empty
      n.next=self.start   #Then put start reference in new node next 
      n.prev=self.start.prev  #and put start prev reference into new node prev
      self.start.prev.next=n   #This is last node and here put new node's reference
      self.start.prev=n        #this is new node's reference put into first prev
    self.start=n  #it's new node's reference in start it have to put both block that's why it outside the blocks
    
  def insert_at_last(self,data):
    n=Node(data)
    if self.is_empty():
      n.next=n
      n.prev=n
      self.start=n
    else:
      n.next=self.start
      n.prev=self.start.prev
      n.prev.next=n
      self.start.prev=n 
      
  def search(self,data):
    temp=self.start
    if temp==None:
      return None
    if temp.item==data:
      return temp
    else:
      temp=temp.next
    while temp !=self.start:
      if temp.item==data:
        return temp
      temp=temp.next
    return None
     
  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(data)
      n.next=temp.next
      n.prev=temp
      temp.next.prev=n
      temp.next=n 
   
  def print_list(self):
    temp=self.start
    if temp is not None:
      print(temp.item, end='  ')
      temp=temp.next
      while temp is not self.start:
        print(temp.item,end='  ')
        temp=temp.next    
      
     
      
        
  
        
    
    
      
    