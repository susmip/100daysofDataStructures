class BinarySearchTree:
  def __init__(self,value):
    self.value=value
    self.rightChild=None
    self.leftChild=None
def insert(rootnode,values):
  if rootnode.value is None:
    rootnode.value=values
  elif rootnode.value<=values:
    if rootnode.leftChild is None:
      rootnode.leftChild=BinarySearchTree(values)
    else:
      insert(rootnode.leftChild,values)
  else:
    if rootnode.rightChild is None:
      rootnode.rightChild=BinarySearchTree(values)
    else:
      insert(rootnode.rightChild,values)
  return("entered successfully")
def Preorder(rootnode):
  if not rootnode:
     return
  print(rootnode.value)
  Preorder(rootnode.leftChild)
  Preorder(rootnode.rightChild)

BST=BinarySearchTree(None)
print(insert(BST,30))
print(insert(BST,10))
print(insert(BST,40))
Preorder(BST)
