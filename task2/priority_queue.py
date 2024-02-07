class PriorityQueue:
    
    def __init__(self):
            self.queue = []

    def __iter__(self):
            return iter(self.queue)

    def __len__(self):
            return len(self.queue)
        
    def push(self, priority, task):
            self.queue.append(priority)
    
    def __next__(self):
          if self.position < len(self.queue):
                queue = self.queue[self.position]
                self.position += 1
                return queue
          else:
                raise StopIteration
          





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
    
