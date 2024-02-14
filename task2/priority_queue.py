import sys


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter([task[0] for task in self.queue])

    def push(self, task_name, priority):
        self.queue.append((task_name, priority))

        def fce(x):
            return x [1]
        
        self.queue.sort(key=fce)

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError("Priority queue is empty")

        task_name, _ = self.queue.pop(0)  # Při odstraňování vrátíme pouze název úkolu
        return task_name
          





priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Tasks in Priority Order:")
for task in priority_queue:
    print(task)

print("Processing tasks in Priority Order:")
while len(priority_queue) > 0:
    task = priority_queue.pop()
    print("Processing:", task)
    
