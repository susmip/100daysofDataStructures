class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    self.prev=None
class circulyDoubly:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertion(self,value,location):
    newnode=Node(value)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
      newnode.prev=newnode
      newnode.next=newnode
    else:
      if location==0:
        newnode.next=self.head
        self.head.prev=newnode
        newnode.prev=self.tail
        self.tail.next=newnode
        self.head=newnode
      elif location==-1:
        self.tail.next=newnode
        newnode.prev=self.tail
        newnode.next=self.head
        self.head.prev=newnode
        self.tail=newnode
      else:
        index=0
        temp=self.head
        while(index<location-1):
          temp=temp.next
          index+=1 
        nextnode=temp.next
        temp.next=newnode
        newnode.next=nextnode
        newnode.prev=temp
        temp.prev=newnode
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
  def deletion(self,location):
    if self.head is None:
      return "elements are not present"
    else:
      if location==0:
        if self.head==self.tail:
          self.head.prev=None
          self.tail.next=None
          self.head=None
          self.tail=None
        else:
          self.head=self.head.next
          self.head.prev=self.tail
          self.tail.next=self.head
      elif location==-1:
        if self.head==self.tail:
          self.head=None
          self.tail=None
          self.head.prev=None
          self.tail.next=None
        else:
          self.tail=self.tail.prev
          self.tail.next=self.head
          self.head.prev=self.tail
      else:
        index=0 
        temp=self.head
        while(index<location-1):
          index+=1 
          temp=temp.next
        temp.next=temp.next.next
        temp.next.prev=temp
        
dc=circulyDoubly()
dc.traversal()
dc.insertion(34,0)
dc.insertion(39,-1)
dc.insertion(50,-1)
print()
dc.traversal()
dc.deletion(1)
print()
dc.traversal()
