''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if int(arr[j])>int(arr[j+1]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
    print(' '.join(arr))

for x in range(int(input())):
    n=int(input())
    arr=input()
    arr=arr.rstrip(" ")
    arr=arr.split(" ")
    bubblesort(arr)
