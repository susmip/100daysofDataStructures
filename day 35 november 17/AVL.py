from collections import deque as queue
class AVL:
  def __init__(self,data):
    self.data=data
    self.leftChild=None
    self.rightChild=None
    self.height=1 

def preorder(root):
  if root is None:
    return
  print(root.data)
  preorder(root.leftChild)
  preorder(root.rightChild)
  
def getheight(rootnode):
  if not rootnode:
    return 0
  return rootnode.height
def getBalance(rootnode):
  if not rootnode:
    return 0
  return getheight(rootnode.leftChild)-getheight(rootnode.rightChild)
def insertion(rootnode,nodevalue):
  if rootnode is None:
    return AVL(nodevalue)
  elif nodevalue < rootnode.data:
    rootnode.leftChild = insertion(rootnode.leftChild, nodevalue)
  else:
    rootnode.rightChild = insertion(rootnode.rightChild, nodevalue)
  rootnode.height=1+max(getheight(rootnode.leftChild),getheight(rootnode.rightChild))
  balance=getBalance(rootnode)
  if balance > 1 and nodevalue < rootnode.leftChild.data:
        return rightRotate(rootnode)
  if balance > 1 and nodevalue > rootnode.leftChild.data:
        rootNode.leftChild = leftRotate(rootnode.leftChild)
        return rightRotate(rootNode)
  if balance < -1 and nodevalue > rootnode.rightChild.data:
        return leftRotate(rootnode)
  if balance < -1 and nodevalue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootnode.rightChild)
        return leftRotate(rootnode)
  return rootnode
def rightRotate(disbalanceNode):
  newnode=disbalanceNode.leftChild 
  disbalanceNode.leftChild=newnode.leftChild.rightChild
  newnode.rightChild=disbalanceNode
  disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
  newnode.height = 1 + max(getHeight(newnode.leftChild), getHeight(newnode.rightChild))
  return newnode
def leftRotate(disbalanceNode):
  newroot=disbalanceNode.rightChild
  disbalanceNode.rightChild=newroot.rightChild.leftChild
  newroot.leftChild=disbalanceNode
  disbalanceNode.height = 1 + max(getheight(disbalanceNode.leftChild), getheight(disbalanceNode.rightChild))
  newroot.height = 1 + max(getheight(newroot.leftChild), getheight(newroot.rightChild))
  return newroot

newAVL = AVL(5)
newAVL = insertion(newAVL, 10)
newAVL = insertion(newAVL, 15)
newAVL = insertion(newAVL, 20)
preorder(newAVL)


  
