#insertion sorting
#selecting,comparing,inserting and shifting



def insertionsort(arr):
  for i in range(1,len(arr)):
    j=i
    while(arr[j-1]>arr[j]) and j>0:
      nums[j-1],arr[j]=arr[j],arr[j-1]
      j-=1 
    
  return nums

nums=[1,2,4,5,3]
s=insertionsort(nums)
print(s)
      

#time complexity - o(n2)
