import heapq

stones=[2,7,4,1,8,1]


max_heap=[-n for n in stones]
heapq.heapify(max_heap)

while len(max_heap)>1:
    s1=-heapq.heappop(max_heap)
    s2=-heapq.heappop(max_heap)
    if s1>s2:
        heapq.heappush(max_heap,-(s1-s2))
    


if max_heap:
    print( -heapq.heappop(max_heap))

else:
    print(0)