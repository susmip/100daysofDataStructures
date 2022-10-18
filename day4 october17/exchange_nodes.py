class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,list1):
        for x in list1:
            newnode=Node(x)
            if self.head is None:
                self.head=newnode
                newnode.next=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                newnode.next=self.head
                self.tail=newnode
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.value,end=" ")
            temp=temp.next
            if temp==self.head:
                break
    def reverse(self,n):
        temp=self.head
        prev=None
        curr=self.head
        
        while(curr.next!=self.head):
            prev=curr
            curr=curr.next
        curr.next=temp.next
        prev.next=temp
        self.head=curr
        temp.next=self.head
   
SLL=CLL()
n=int(input())
list1=list(map(int,input().split(" ")))
SLL.insert(list1)
SLL.reverse(n)
SLL.traverse()
