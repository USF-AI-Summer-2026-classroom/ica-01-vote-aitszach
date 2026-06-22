class PriorityQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, candidate, priority):
        self.items.append((priority, candidate))
        self.items.sort(key=lambda x: x[0])

    def __iter__(self):
        for priority, candidate in self.items:
            yield candidate