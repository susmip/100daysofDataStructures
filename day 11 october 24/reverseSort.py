def selection(arr):
    for i in range(len(arr)):
        maxindex=i 
        for j in range(i+1,len(arr)):
            if arr[j]>arr[maxindex]:
                maxindex=j 
        arr[i],arr[maxindex]=arr[maxindex],arr[i]
    return(arr)


n=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
k=selection(arr)
for x in k:
    print(x,end=" ")



