

l=[2,1,5,3,1,0,4]

#initiating

def findWaterLevel(arr,x):
    leftmax,rightmax=x,x
    for i in range(0,x):
        if arr[i]>arr[leftmax]:
            leftmax=i

    for i in range(x+1,len(l)):
        if arr[i]>arr[rightmax]:
            rightmax=i


    return min(arr[leftmax],arr[rightmax])-arr[x]




lmax,rmax=l[0],l[-1]
left=1
right=len(l)-2
level=0
while left<right:
    if lmax<rmax:
        level+=findWaterLevel(l,left)
        left+=1
    
        if l[left]>lmax:
            lmax=l[left]
        

    else:
        level+=findWaterLevel(l,right)
        right-=1
        if l[right]>rmax:
            rmax=l[right]

print(level)


