class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class SinglyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertSLL(self,value,position):
    newnode=Node(value)
    if self.head is None:
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
        while loc<position-1:
          if temp.next==None:
            break
          temp=temp.next
          loc+=1 
        nextnode=temp.next
        temp.next=newnode
        newnode.next=nextnode
        if temp==self.tail:
          self.tail=newnode
  def Traverse(self):
    if self.head==None:
      print("Empty List")
    else:
      temp=self.head
      while temp is not None:
        print(temp.value,end=" ")
        temp=temp.next
        
  def length(self):
    temp=self.head
    length=0
    while temp is not None:
      length+=1 
      temp=temp.next 
    return length
  def middle(self):
    length=self.length()//2
    temp=self.head
    loc=0
    while loc<length:
      temp=temp.next
      loc+=1 
    print(temp.value)
    
          
          
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 3)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(7, -1)
singlyLinkedList.insertSLL(5, 6)
singlyLinkedList.insertSLL(9, -1)
singlyLinkedList.insertSLL(8, -1)
singlyLinkedList.Traverse()
print()        
singlyLinkedList.middle()   
      
