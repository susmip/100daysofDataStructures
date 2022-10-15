class Solution:
    def __init__(self,lists):
        self.lists=lists
    def reverse(self):
        output=[]
        stack=[]
        for x in self.lists:
            if x%2==0:
                stack.insert(0,x)
            elif x%2!=0:
                output.extend(stack)
                stack=[]
                output.append(x)
        output.extend(stack)
        return output

n=int(input())
lists=list(map(int,input().split(' ')))
solution=Solution(lists)
list1=solution.reverse()
for x in list1:
    print(x,end=" ")
