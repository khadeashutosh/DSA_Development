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
  
        
    
    
      
    