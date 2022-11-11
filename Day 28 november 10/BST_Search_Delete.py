class BinarySearchTree:
  def __init__(self,value):
    self.value=value
    self.left=None
    self.right=None

def insert(root,ivalue):
  if root.value is None:
    root.value=ivalue
  elif root.value>=ivalue:
    if root.left is None:
      root.left=BinarySearchTree(ivalue)
    else:
      insert(root.left,ivalue)
  else:
    if root.right is None:
      root.right=BinarySearchTree(ivalue)
    else:
      insert(root.right,ivalue)
  return "entered successfully"
def preorder(root):
  if root is None:
    return
  print(root.value)
  preorder(root.left)
  preorder(root.right)

def search(root,svalue):
  if root.value==svalue:
    print("value found")
  elif svalue<root.value:
    if root.left.value==svalue:
      print("value found")
    else:
      search(root.left,svalue)
  else:
    if root.right.value==svalue:
      print("value found")
    else:
      search(root.right,svalue)
def minvalue(root):
  curr=root
  while(curr.left is not None):
    curr=curr.left
  return curr
def deletion(root,dvalue):
  if root is None:
    return root
  if dvalue<root.value:
    root.left=deletion(root.left,dvalue)
  elif dvalue>root.value:
    root.right=deletion(root.right,dvalue)
  else:
    if root.left is None:
      temp=root.right
      root=None
      return temp
    if root.right is None:
      temp=root.left
      root=None
      return temp
    temp=minvalue(root.right)
    root.value=temp.value
    root.right=deletion(root.right,temp.value)
  return root
    
    
    
  


BST=BinarySearchTree(None)
insert(BST,40)
insert(BST,30)
insert(BST,50)
preorder(BST)
try:
  search(BST,40)
except:
  print("value not found")

deletion(BST,10)
preorder(BST)
