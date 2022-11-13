class BinarySearchTree:
  def __init__(self,value):
    self.value=value
    self.rightChild=None
    self.leftChild=None

def insertNode(rootnode,values):
    if rootnode.value is None:
      rootnode.value=values
    elif rootnode.value>=values:
      if rootnode.leftChild is None:
        rootnode.leftChild=BinarySearchTree(values)
      else:
        insertNode(rootnode.leftChild,values)
    else:
      if rootnode.rightChild is None:
        rootnode.rightChild=BinarySearchTree(values)
      else:
        insertNode(rootnode.rightChild,values)
    return "entered successfully"


def searchNode(rootNode, nodeValue):
    if rootNode.value == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.value:
        if rootNode.leftChild.value == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.value == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

def minvalue(rootNode):
  curr=rootNode
  while(curr.leftChild is not None):
    curr=curr.leftChild
  return curr

def delete(rootNode,dvalue):
  if rootNode is None:
    return rootNode
  if dvalue<rootNode.value:
    rootNode.leftChild=delete(rootNode.leftChild,dvalue)
  elif dvalue>rootNode.value:
    rootNode.rightChild=delete(rootNode.rightChild,dvalue)
  else:
    if rootNode.leftChild is None:
      temp=rootNode.rightChild
      rootNode=None
      return temp
    if rootNode.rightChild is None:
      temp=rootNode.leftChild
      rootNode=None
      return temp
    temp=minvalue(rootNode.rightChild)
    rootNode.value=temp.value
    rootNode.rightChild=delete(rootNode.rightChild,temp.value)
  return rootNode
  
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"

def preorder(root):
  if root is None:
    return
  print(root.value)
  preorder(root.leftChild)
  preorder(root.rightChild)

import collections
def levelorder(root):
  result=[]
  queue=collections.deque()
  queue.append(root)
  while queue:
    level=[]
    qlen=len(queue)
    for i in range(len(queue)):
      node=queue.popleft()
      if node:
        level.append(node.value)
        queue.append(node.leftChild)
        queue.append(node.rightChild)
    if level:
      result.append(level)
  return result
    
  
  

BST=BinarySearchTree(None)
print(insertNode(BST,30))
print(insertNode(BST,10))
print(insertNode(BST,40))
print(insertNode(BST,60))
searchNode(BST,10)
delete(BST,20)
preorder(BST)
print(levelorder(BST))
