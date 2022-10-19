class Node:
  def __init__(self,value):
    self.value=value
    self.prev=None
    self.next=None
class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertion(self,value,location):
    newnode=Node(value)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
      newnode.prev=None
      newnode.next=None
    else:
      if location==0:
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
      elif location==-1:
        self.tail.next=newnode
        newnode.prev=self.tail
        self.tail=newnode
      else:
        index=0
        temp=self.head
        while index<location-1:
          temp=temp.next
          index+=1 
        nextnode=temp.next
        temp.next=newnode
        newnode.prev=temp
        newnode.next=nextnode
        nextnode.prev=newnode
  def traverse(self):
    if self.head==None:
      print("No elements")
    else:
      temp=self.head
      while(temp!=None):
        print(temp.value,end=" ")
        temp=temp.next
  def deletion(self,location):
    if self.head is None:
      print("No elements found")
    else:
      if location==0:
        if self.head==self.tail:
          self.head=None
          self.head=None
        else:
          self.head=self.head.next
          self.head.prev=None
      elif location==-1:
        if self.head==self.tail:
          self.head=None
          self.tail=None
        else:
          self.tail=self.tail.prev
          self.tail.next=None
      else:
        temp=self.head
        index=0
        while(index<location-1):
          temp=temp.next
          index+=1 
        temp.next=temp.next.next
        temp.next.prev=temp
  def deleteAll(self):
    if self.head==None:
      print("empty list")
    else:
      temp=self.head
      while temp is not None:
        temp.prev=None
        temp=temp.next
    
        

doubly=DoublyLinkedList()
doubly.insertion(1,1)
doubly.insertion(4,0)
doubly.insertion(6,-1)
doubly.insertion(5,-1)
doubly.insertion(8,-1)
doubly.traverse()
doubly.deletion(1)
print()
doubly.traverse()
