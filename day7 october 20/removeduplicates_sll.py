class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SinglyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertion(self,value):
        newnode=Node(value)
        if self.head is None:
            
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.next=None
            self.tail=newnode
    def printduplicates(self):
        temp=self.head
        stack=[]
        while temp is not None:
            stack.append(temp.value)
            temp=temp.next
        return stack

SLL=SinglyLinkedlist()
for x in range(int(input())):
    SLL.insertion(int(input()))
s=SLL.printduplicates()
for x in s:
    if s.count(x)>1:
        print(x)
