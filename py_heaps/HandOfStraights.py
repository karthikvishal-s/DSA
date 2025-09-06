from collections import deque,Counter
import heapq

def isNStraightHand(hand,groupSize):

    if len(hand)%groupSize!=0:
        return False

    count=Counter(hand)

    minheap = list(count.keys())

    heapq.heapify(minheap)
    first = minheap[0]
    for i in range(first,first+groupSize):
        if i not in minheap:
            return False
        count[i]-= 1
        if count[i]==0:
            if i!=minheap[0]:
                return False
            heapq.heappop(minheap)

    return True

print(isNStraightHand([1,2,3,6,2,3,4,7,8,],3))  # Output: True