''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,list1):
        if type(list1)==list:
            for x in list1:
                newnode=Node(x)
                if self.head is None:
                    self.head=newnode
                    self.tail=newnode
                    newnode.next=newnode
                else:
                    newnode.next=self.head
                    self.tail.next=newnode
                    self.tail=newnode
        elif type(list1)==int:
            newnode=Node(list1)
            newnode.next=self.head
            self.tail.next=newnode
            self.tail=newnode
            

    def Traverse(self):
        temp=self.head
        while temp:
            print(temp.value,end=" ")
            temp=temp.next
            if temp==self.head:
                break

SLL=SinglyLinkedList()
n=int(input())
list1=list(map(int,input().split(" ")))
SLL.insert(list1)
n=int(input())
SLL.insert(n)
SLL.Traverse()


