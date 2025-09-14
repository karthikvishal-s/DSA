# Longest Increasing Subsequence

l=[3,4,5,1,2,3,4]

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
            if res[mid]>l[i]:
                right=mid
            else:
                left=mid+1
        res[left]=l[i]

print(len(res))
