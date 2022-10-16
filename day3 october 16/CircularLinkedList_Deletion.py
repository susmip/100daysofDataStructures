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
  def DeletionCSLL(self,location):
    if self.head is None:
      return "Linked list is empty"
    else:
      if location==0:
        if self.head==self.tail:
          self.head=None
          self.head.next=None
          self.tail=None
        else:
          self.head=self.head.next
          self.tail.next=self.head
      elif location==-1:
        if self.head == self.tail:
          self.head.next = None
          self.head = None
          self.tail = None
        else:
          temp=self.head
          while temp is not None:
            if temp.next==self.tail:
              break
            temp=temp.next 
          temp.next=self.head
          self.tail=temp
      else:
        tempNode = self.head
        index = 0
        while index < location - 1:
          tempNode = tempNode.next
          index += 1
        nextNode = tempNode.next
        tempNode.next = nextNode.next
  def deleteEntireCSLL(self):
    self.head=None
    self.tail.next=None
    self.tail=None
          
          

circularSLL = CircularLinkedList()
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,0)
circularSLL.traversalCSLL()
circularSLL.deleteEntireCSLL()
print()
circularSLL.traversalCSLL()
