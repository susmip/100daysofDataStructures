class Bnode:
  def __init__(self,values):
    self.values=values
    self.rightChild=None
    self.leftChild=None

def insertion(rootnode,value):
  if rootnode.values is None:
    rootnode.values=value
  elif rootnode.values>=value:
    if rootnode.leftChild is None:
      rootnode.leftChild=Bnode(value)
    else:
      insertion(rootnode.leftChild,value)
  else:
    if rootnode.rightChild is None:
      rootnode.rightChild=Bnode(value)
    else:
      insertion(rootnode.rightChild,value)
def preorder(rootnode):
  if not rootnode:
    return "no elements"
  print(rootnode.values)
  preorder(rootnode.leftChild)
  preorder(rootnode.rightChild)
  
def search(rootnode,value):
  if rootnode.values==value:
    print("value found")
  elif value<rootnode.values:
    if rootnode.leftChild.values==value:
      print("value found")
    else:
      search(rootnode.leftChild,value)
  else:
    if rootnode.rightChild.values==value:
      print("value found")
    else:
      search(rootnode.rightChild,value)
      
def minvalue(rootNode):
  curr=rootNode
  while(curr.leftChild is not None):
    curr=curr.leftChild
  return curr
  
def deletion(rootnode,dvalue):
  if rootnode is None:
    return "no nodes"
  if rootnode.values>dvalue:
    rootnode.leftChild=deletion(rootnode.leftChild,dvalue)
  elif rootnode.values<dvalue:
    rootnode.rightChild=deletion(rootnode.rightChild,dvalue)
  else:
    if rootnode.leftChild is None:
      temp=rootnode.rightChild
      rootnode=None
      return temp
    if rootnode.rightChild is None:
      temp=rootnode.leftChild
      rootnode=None
      return temp
    temp=minvalue(rootnode.rightChild)
    rootnode.values=temp.values
    rootNode.rightChild=delete(rootNode.rightChild,temp.values)
  return rootnode
    

BT=Bnode(8)
insertion(BT,7)
insertion(BT,6)
preorder(BT)
try:
  search(BT,7)
except:
  print("value not found")
deletion(BT,6)
preorder(BT)
