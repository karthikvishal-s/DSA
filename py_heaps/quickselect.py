nums=[3,2,4,2,1,4,5,2,8,10]
k=1
k=len(nums)-k

def quickselect(l,r):
    pivot,p = nums[r],l
    for i in range(l,r):
        if nums[i]<=pivot:
            nums[i],nums[p]=nums[p],nums[i]
            p+=1
    nums[p],nums[r]=nums[r],nums[p]

    if k<p:
        return quickselect(l,p-1)
    elif k>p:
        return quickselect(p+1,r)
    else:
        return nums[p]

print(quickselect(0,len(nums)-1) )