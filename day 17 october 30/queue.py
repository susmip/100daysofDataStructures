class queue:
  def __init__(self):
    self.queue=[]
  def __str__(self):
    list1=[str(x) for x in self.queue]
    return(' '.join(list1))
  def isempty(self):
    if self.queue==[]:
      return True 
    else:
      return False
  def enqueue(self,val):
    self.queue.append(val)
  def dequeue(self):
    if self.isempty():
      return "no elements"
    else:
      ele = self.queue.pop(0)
  def peek(self):
    return self.queue[0]

q=queue()
q.enqueue(5)  
q.enqueue(7)
q.enqueue(8)
q.enqueue(10)
print(q)
q.dequeue()
print(q)
k=q.peek()
print(k)
  
