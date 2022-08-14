import heapq


l=[15,7,5,3,15,9,14,3]

heapq.heapify(l)

print(l)


heapq.heappush(l,30)
print(l)

heapq.heappush(l,3)
print(l)

heapq.heappop(l)
print(l)
