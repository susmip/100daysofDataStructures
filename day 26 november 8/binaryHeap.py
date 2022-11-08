class BinaryHeap:
  def __init__(self):
    self.heapList=[]
    self.currentsize=0
  def percUP(self,i):
    while(i//2>0):
      if self.heapList[i]<self.heapList[i//2]:
        self.heapList[i//2],self.heapList[i]=self.heapList[i],self.heapList[i//2]
      i=i//2
  def insert(self,value):
    self.heapList.append(value)
    self.currentsize+=1 
    self.percUP(self.currentsize)
  def percDown(self,i):
    while(i*2<=self.currentsize):
      m=self.minChild(i)
      if self.heapList[i]>self.heapList[mc]:
        self.heapList[mc],self.heapList[i]=self.heapList[i],self.heapList[mc]
      i=mc 
  def minChild(self,i):
    if i*2+1>self.currentsize:
      return i*2
    else:
      if self.heapList[i*2] < self.heapList[i*2+1]:
        return i * 2
      else:
        return i * 2 + 1
        
  
bh=BinaryHeap()
bh.insert(7)
bh.insert(8)
bh.insert(5)
