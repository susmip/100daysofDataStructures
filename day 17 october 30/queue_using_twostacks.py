
#hackerrank
# Enter your code here. Read input from STDIN. Print output to STDOUT
class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,ele):
        self.queue.append(ele)
    def dequeue(self):
        self.queue.pop(0)
    def peek(self):
        return self.queue[0]

q=queue()
for x in range(int(input())):
    list1=list(input().split(" "))
    if list1[0]=='1':
        q.enqueue(list1[-1])
    if list1[0]=='2':
        q.dequeue()
    if list1[0]=='3':
        k=q.peek()
        print(k)
