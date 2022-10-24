''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(arr):
    fives=[]
    nonfive=[]
    for x in arr:
        if x%5==0:
            fives.append(x)
        else:
            nonfive.append(x)
            
    fives.sort()
    fives.extend(nonfive)
    return fives

n=int(input())
arr=list(map(int,input().split(" ")))
k=main(arr)
for x in k:
    print(x,end=" ")
