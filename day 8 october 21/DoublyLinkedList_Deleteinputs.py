''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertion(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            newnode.next= None
            self.tail=newnode
            newnode.prev=None
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            newnode.next=None
            self.tail=newnode
    def search(self,svalue):
        index=0
        temp=self.head
        while temp:
            if temp.value==svalue:
                return index
                break
            index+=1
            temp=temp.next
    def deletion(self,position):
        index=0
        temp=self.head
        while(index<position-1):
          index+=1 
          temp=temp.next
        nextnode=temp.next.next
        temp.next=nextnode
        nextnode.prev=temp
    def traversal(self):
        if self.head==None:
            print("No elements")
        else:
            output=[]
            temp=self.head
            while(temp!=None):
                output.append(temp.value)
                temp=temp.next
            return ' '.join(output)


DLL=DoublyLinkedList()
for x in range(int(input())):
    DLL.insertion(input())
print()
for x in range(int(input())):
    inp=input().strip(" ")
    pos=DLL.search(inp)
    DLL.deletion(pos)
s=DLL.traversal()
print(s)




