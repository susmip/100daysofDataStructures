class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    self.prev=None

class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  def insertion(self,val,pos):
    node=Node(val)
    if self.head==None:
      self.head=node
      node.prev=None
      node.next=None
      self.tail=node
    else:
      if pos==0:
        node.prev=None
        node.next=self.head
        self.head.prev=node
        self.head=node
      elif pos==-1:
        node.prev=self.tail
        self.tail.next=node
        self.tail=node
        node.next=None
      else:
        index=0
        temp=self.head
        while(index<pos-1):
          temp=temp.next
          index+=1 
        nextnode=temp.next
        temp.next=node
        nextnode.prev=node
        node.prev=temp
        node.next=nextnode
        
  def traverse(self):
    if self.head==None:
      print("No elements")
    else:
      temp=self.head
      while(temp!=None):
        print(temp.value,end=" ")
        temp=temp.next
        

doubly=DoublyLinkedList()
doubly.insertion(1,1)
doubly.insertion(4,0)
doubly.insertion(6,-1)
doubly.traverse()
        
        
