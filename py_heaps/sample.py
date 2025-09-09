import heapq

l=[1,2,3,4,5,0]


print(l)
heapq.heapify(l)
print(l)

while l:
    print(heapq.heappop(l))