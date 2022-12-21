#Write a function that takes in two numbers and recursively multiplies them together

def multiplies(n1,n2):
  if n2==1:
    return n1*1
  print(n1*n2)
  return multiplies(n1,n2-1)
  
print(multiplies(4,6))


print()
#Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to use the ** operator!

def power(base,exp):
  if exp==0:
    return 1 
  return base*power(base,exp-1)

print(power(2,5))
print()
#Write a function using recursion to print numbers from n to 0.

def printnumbers(n):
  if n==0:
    print(n)
    return
  print(n)
  printnumbers(n-1)
  
print(printnumbers(10))
print()
  
#Write a function using recursion to print numbers from 0 to n (you just need to change one line in the program of problem 1)
def printnumbers2(n,i):
  if i==n:
    print(i)
    return
  print(i)
  printnumbers2(n,i+1)
  
print(printnumbers2(10,0))
print()

#Write a function using recursion that takes in a string and returns a reversed copy of the string. The only string operation you are allowed to use is string concatenation
def reverse(string):
  if len(string)==1:
    return string
  return(string[-1]+reverse(string[:-1]))

print(reverse('Run to you'))
print()


#fibonacci

def fibonacci(n):
  if n==0 or n==1:
    return n 
  return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(9))
  
  
