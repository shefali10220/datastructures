from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, val):
        print("Value Added",val)
        self.queue.appendleft(val)

    def popp(self):
        print("Value Removed",self.queue[-1])
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        print("Size of the Queue is :" ,len(self.queue))


pq = Queue()

pq.push({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.push({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.push({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

pq.size()
pq.popp()