import heapq
nums1=[3,1,2,4]

heapq.heapify(nums1)
print("Heapified List:", nums1)

print("Peek:", nums1[0])

nums2=[3,2,4,1]
max_heap=[-n for n in nums2]
heapq.heapify(max_heap)
print("Max-Heapified List:", [-n for n in max_heap])
print("Max Peek:", -max_heap[0])