class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueu(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)


queue = Queue()
# print(queue.is_empty())
queue.enqueu(2)
queue.enqueu(4)
queue.enqueu(3)
queue.enqueu(6)
# print(queue.peek())
# print(queue.items)
# print(queue.dequeue())
print(queue.size())