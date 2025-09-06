

from collections import Counter
import heapq
n=2
count=Counter([1,2,3,6,2,3,4,7,8])

maxheap=[[-count[i],i] for i in count]
heapq.heapify(maxheap)
print(maxheap)

res=[]
while n>0:
    res.append(heapq.heappop(maxheap)[1])
    n-=1
print(res)


