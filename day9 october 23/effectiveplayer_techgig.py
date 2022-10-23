def main(array):
    for i in range(1,len(array)):
        j=i 
        while(arr[j-1]<arr[j] and j>0):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return array

dict1={}
arr=[]
for x in range(int(input())):
    name,val=input().split(" ")
    dict1[val]=name
    arr.append(int(val))
array=main(arr)
for x in arr:
    print(dict1[str(x)])
