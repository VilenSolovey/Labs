"""Lab 4"""

class Node():
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class BinaryHeap():
    def __init__(self):
        self.queue = []

    def add_element(self, value, priority):
        new_node = Node(value, priority)
        self.queue.append((new_node.value, new_node.priority))
        queue_width = len(self.queue) - 1
        self.up(queue_width)

    def pop_elem(self):
        deleted_elem = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.down(0)
        return deleted_elem

    def up(self, element_count):
        while element_count > 0:
            father = (element_count - 1) // 2
            if self.queue[element_count][1] > self.queue[father][1]:
                self.queue[element_count], self.queue[father] = self.queue[father], self.queue[element_count]
                element_count = father
            else:
                break

    def down(self, r):
        while True:
            left, right = 2 * r + 1, 2 * r + 2
            biggest = r
            if left < len(self.queue) and self.queue[left][1] > self.queue[biggest][1]:
                biggest = left
            if right < len(self.queue) and self.queue[right][1] > self.queue[biggest][1]:
                biggest = right
            if biggest == r:
                break
            self.queue[r], self.queue[biggest] = self.queue[biggest], self.queue[r]
            r = biggest

    def peak_queue(self):
        if len(self.queue) > 0:
            print(self.queue)
        else:
            return None
