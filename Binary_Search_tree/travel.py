class Node:
  def __init__(self,item=None,left=None,  right=None):
    self.item=item
    self.left=left
    self.right=right
    
class BTS:
  def __init__(self,root=None)    :
    self.root=root
  
  def insert(self,data):
    self.root=self.recursion_insert(self.root,data) 
  def recursion_insert(self,root,data):
    if root is None:
      return Node(data)
    if data <root.item:
      root.left=self.recursion_insert(root.left,data)
    elif data> root.item:
      root.right=self.recursion_insert(root.right,data)
    return root      
     
  def search(self,data):
    return self.recursion_search(self.root,data)  
    
  def recursion_search(self,root,data):
    if root is None or root.item==data  :
      return root
    
    if data<root.item:
      return self.recursion_search(root.left,data)
    
    else:
      return self.recursion_search(root.right,data)
      
  def inorder(self):
    result=[]
    self.recursion_inorder(self.root,result)
    return result

  def recursion_inorder(self,root,result):
    if root :
      self.recursion_inorder(root.left,result) 
      result.append(root.item)
      self.recursion_inorder(root.right,result) 
      
  def preorder(self):
    result=[]
    self.recursion_preorder(self.root,result)
    return result

  def recursion_preorder(self,root,result):
    if root :
      result.append(root.item)
      self.recursion_preorder(root.left,result)
      self.recursion_preorder(root.right,result)     

  def postorder(self):
    result=[]
    self.recursion_postorder(self.root,result)
    return result

  def recursion_postorder(self,root,result):
    if root :
      self.recursion_postorder(root.left,result)
      self.recursion_postorder(root.right,result)   
      result.append(root.item)      