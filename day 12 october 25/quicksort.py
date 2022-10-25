def quicksort(array,low,high):
  pivot=array[high]
  i=low-1
  for j in range(low,high):
    if array[j]<pivot:
      i+=1
      array[i],array[j]=array[j],array[i]
  array[i+1],array[high]=array[high],array[i+1]
  return(i+1)

def quick(array,low,high):
  if low<high:
    pi=quicksort(array,low,high)
    quick(array,low,pi-1)
    quick(array,pi+1,high)

array = [ 10, 7, 8, 9, 1, 5]
quick(array, 0, len(array) - 1)
print(array)
