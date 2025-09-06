from queue import PriorityQueue

pq=PriorityQueue()

pq.put((3,"Task A"))
pq.put((1,"Task B"))
pq.put((2,"Task C"))
pq.put((4,"Task D"))

print("Peak:", pq.queue[0])

while not pq.empty():
    print("pop: ",pq.get())