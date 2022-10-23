''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def extends(sixes,output):
    sixes.sort()
    sixes.append(sum(sixes))
    output.extend(sixes)
    return output

def main(arr):
    sixes=[]
    twos=[]
    three=[]
    output=[]
    for i in range(0,len(arr)):
        if arr[i]%6==0:
            sixes.append(arr[i])
        elif arr[i]%2==0:
            twos.append(arr[i])
        elif arr[i]%3==0:
            three.append(arr[i])
    output=extends(sixes,output)
    output=extends(twos,output)
    output=extends(three,output)
    return output


n=int(input())
string=input().rstrip(" ")
arr=list(map(int,string.split(" ")))
j=main(arr)
for x in j:
    print(x, end=" ")
