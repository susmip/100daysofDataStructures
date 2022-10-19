class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertion(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.next=None
            self.tail=newnode
    def remove(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            if temp==self.tail:
                break
            

singly=SLL()
for x in range(int(input())):
    n=int(input())
    singly.insertion(n)
singly.remove()
