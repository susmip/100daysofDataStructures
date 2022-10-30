class CircularQueue:
  def __init__(self,capacity):
    self.capacity=capacity
    self.queue=[None]*self.capacity
    self.front=-1
    self.rear=-1
  def __str__(self):
    list1=[str(x) for x in self.queue]
    return(' '.join(list1))
  def isFull(self):
    if self.front==0 and self.rear+1==self.capacity:
      return True
    if self.rear+1==self.front:
      return True
    else:
      return False
  def isEmpty(self):
    if self.front==-1:
      return True
    else:
      return False
  def enqueue(self,ele):
    if self.isFull():
      return "queue is full"
    else:
      if self.rear+1==self.capacity:
        self.rear=0
      else:
        self.rear+=1 
        if self.front==-1:
          self.front=0
    self.queue[self.rear]=ele
  def dequeue(self):
    if self.isEmpty():
      return "No elements"
    else:
      start=self.front
      element=self.queue[start]
      if self.front==self.rear:
        self.front=-1
        self.rear=-1
      elif self.front+1==self.capacity:
        self.front=0
      else:
        self.front+=1 
    self.queue[start]=None
    return element
  def peek(self):
    if self.isEmpty():
      return "There is not any element in the Queue"
    else:
      return self.queue[self.front]


customQueue = CircularQueue(3)
customQueue.enqueue(8)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.enqueue(1)
print(customQueue)
print(customQueue.peek())
