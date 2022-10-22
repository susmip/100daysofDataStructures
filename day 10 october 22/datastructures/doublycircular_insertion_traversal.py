class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    self.prev=None

class DoublyCircular:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertion(self,value,location):
    newnode=Node(value)
    if self.head is None:
      self.head=newnode
      self.tail=newnode
      newnode.next=newnode
      newnode.prev=newnode
    else:
      if location==0:
        self.head.prev=newnode
        newnode.next=self.head
        newnode.prev=self.tail
        self.head=newnode
      elif location==-1:
        self.tail.next=newnode
        newnode.prev=self.tail
        newnode.next=self.head
        self.tail=newnode
      else:
        index=0
        temp=self.head
        while(index<location-1):
          index+=1 
          temp=temp.next
        nextnode=temp.next
        temp.next=newnode
        newnode.prev=temp
        newnode.next=nextnode
        nextnode.prev=newnode
  def traversal(self):
    temp=self.head
    if self.head==None:
      print("No elements")
    else:
      while temp:
        print(temp.value,end=" ")
        temp=temp.next
        if temp==self.tail.next:
          break



dc=DoublyCircular()
dc.insertion(34,0)
dc.insertion(39,-1)
dc.insertion(50,-1)
dc.insertion(49,1)
print()
dc.traversal()  
