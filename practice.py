from collections import defaultdict
from queue import PriorityQueue


d = defaultdict(list)

d['python'].append("awesome")
d['something-else'].append("irrelvent")
d['python'].append("language")

for i in d.items():
	print(i)

print("hello")	

print("Priority Queue starts here")

pq = PriorityQueue()
d_dict1 = (3, 'A')
d_dict2 = (1,'X')
d_dict3 = (2,'C')

pq.put(d_dict1)
pq.put(d_dict2)
pq.put(d_dict3)

print("Priority queue before getting:")
print(pq.queue)

while not pq.empty():
	next_item  = pq.get()
	print(next_item)


