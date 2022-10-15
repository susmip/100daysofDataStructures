class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class SLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertSLL(self,value,position):
    newnode=Node(value)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
    else:
      if position==0:
        newnode.next=self.head
        self.head=newnode
      elif position==-1:
        newnode.next=None
        self.tail.next=newnode
        self.tail=newnode
      else:
        loc=0
        temp=self.head
        while(loc<position-1):
          if temp.next==None:
            break
          temp=temp.next
          loc+=1
        nextnode=temp.next
        temp.next=newnode
        newnode.next=nextnode
        if temp == self.tail:
          self.tail=newnode
  def reverse(self):
    reverseList=[]
    temp=self.head
    while temp is not None:
      reverseList.insert(0,str(temp.value))
      temp=temp.next
    return ' '.join(reverseList)
  def Traverse(self):
    if self.head==None:
      print("Empty List")
    else:
      temp=self.head
      while temp is not None:
        print(temp.value,end=" ")
        temp=temp.next

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 3)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(7, -1)
singlyLinkedList.insertSLL(5, 6)
singlyLinkedList.Traverse()
print()
print(singlyLinkedList.reverse())
