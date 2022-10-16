class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class CircularLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertCSLL(self,value,position):
    newnode=Node(value)
    if self.head is None:
      self.head=newnode
      self.tail=newnode
      newnode.next=newnode
    else:
      if position==0:
        newnode.next=self.head
        self.head=newnode
        self.tail.next=newnode
      elif position==-1:
        newnode.next=self.head
        self.tail.next=newnode
        self.tail=newnode
      else:
        tempNode = self.head
        index = 0
        while index < position - 1:
          tempNode = tempNode.next
          index += 1
        nextnode=tempNode.next
        tempNode.next=newnode
        newnode.next=nextnode
        if tempNode == self.tail:
          self.tail=newnode
  def traversalCSLL(self):
    if self.head is None:
      print("There is not any element for traversal")
    else:
      tempNode = self.head
      while tempNode:
        print(tempNode.value, end=" ")
        tempNode = tempNode.next
        if tempNode == self.tail.next:
          break

circularSLL = CircularLinkedList()
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,0)
circularSLL.traversalCSLL()

