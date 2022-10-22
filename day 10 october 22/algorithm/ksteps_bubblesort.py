''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def bubblesort(arr,k):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if int(arr[j])>int(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
        
        if k>0:
            print(' '.join(arr))
            k-=1


n=int(input())
for x in range(n):
    eler,k=list(map(int,input().split(" ")))
    ele=input().rstrip(" ")
    ele=ele.split(" ")
    print(ele)
    bubblesort(ele,k)
