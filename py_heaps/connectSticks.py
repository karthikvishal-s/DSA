import heapq

sticks = [2,4,3]


minheap=sticks
heapq.heapify(minheap)
cost = 0

while len(minheap)>1:
    first = heapq.heappop(minheap)

    second = heapq.heappop(minheap)

    cost = cost+first+second
 
    heapq.heappush(minheap,first+second)


print(cost)