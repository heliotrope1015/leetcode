# n=int(raw_input())
# nums=raw_input()

n=2
nums="1 8"
numslist=map(int,nums.split(' '))
result=[]
# print numslist
for i in range(n):
    arr=[0]*(numslist[i]*4)
    # print arr
    j=0
    count=0
    while arr[j]==0 :
        arr[j]=1
        j=j+numslist[i]+1
        count+=1
        if j>=len(arr):
            j=j-len(arr)
    result.append(count)
for i in result:
    print i+1