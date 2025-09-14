# Longest Increasing Subsequence

l=[4,10,4,3,8,9]

# using binary search algorithm

res=[]
res.append(l[0])

for i in range(1,len(l)):
    if l[i]>res[-1]:
        res.append(l[i])

    else:
        
        left,right=0,len(res)-1
        while left<right:

            mid=(left+right)//2
            if res[mid]>=l[i]:
                right=mid
            else:
                left=mid+1
        res[left]=l[i]

    print(res)

print(len(res))
