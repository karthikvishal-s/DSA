import heapq
nums=[3,2,1,5,6,4]
k=2


max_heap=[-n for n in nums]
heapq.heapify(max_heap)
count=1
while count<k:
    heapq.heappop(max_heap)
    count+=1

print(-max_heap[0])