class Tree:
  def __init__(self,value):
    self.value=value
    self.right=None
    self.left=None
  def insertLeft(self,newvalue):
    if self.left is None:
      self.left=Tree(newvalue)
    else:
      t=Tree(newvalue)
      t.leftchild=self.left
      self.left=t
  def insertRight(self,newvalue):
    if self.right is None:
      self.right=Tree(newvalue)
    else:
      t=Tree(newvalue)
      t.right=self.right
      self.right=t
  def GetRightChild(self):
    return self.right
  def GetLeftChild(self):
    return self.left  
  def Getrootnode(self):
    return self.value 
  def setRootNode(self,obj):
    self.root=obj 
def preorder(root):
  if root:
    print(root.Getrootnode(),end=" ")
    preorder(root.GetLeftChild())
    preorder(root.GetRightChild())
def inorder(root):
  if root:
    inorder(root.GetLeftChild())
    print(root.Getrootnode(),end=" ")
    inorder(root.GetRightChild())
def postorder(root):
  if root:
    postorder(root.GetLeftChild())
    postorder(root.GetRightChild())
    print(root.Getrootnode(),end=" ")
  
  
  
t=Tree(5)
t.insertLeft(6)
t.insertRight(8)
k=t.GetLeftChild().Getrootnode()
print(k)
preorder(t)
print()
inorder(t)
print()
postorder(t)
    
