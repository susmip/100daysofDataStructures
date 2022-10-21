#BUBBLE SORT 
#COMPARISION AND SORTING
def bubblesort(nums):
  for i in range(len(nums)-1,0,-1):
    for j in range(i):
      if nums[j]>nums[j+1]:
        nums[j],nums[j+1]=nums[j+1],nums[j]
  return nums
      
    
nums=[9,8,2,3,1]
k=bubblesort(nums)
print(k)


