import heapq
nums=[3,2,1,5,6,4]
k=2


l=[-n for n in nums]
heapq.heapify(l)
count=1
while count<k:
    heapq.heappop(l)
    count+=1

print(-l[0])