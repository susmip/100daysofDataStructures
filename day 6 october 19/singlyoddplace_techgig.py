''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertion(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.next=None
            self.tail=newnode
    def traverse(self):
        index=0
        temp=self.head
        while temp is not None:
            if index%2!=0:
                print(temp.value)
            temp=temp.next
            index+=1

singly=SLL()
for x in range(int(input())):
    n=int(input())
    singly.insertion(n)
singly.traverse()
