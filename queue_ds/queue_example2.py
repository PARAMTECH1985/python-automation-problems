from collections import deque
queue = deque()
# Enqueue
queue.append('X')
queue.append('Y')
queue.append('Z')
print(f"Queue after enqueuing: {queue}")

# Dequeue
dequeued_item = queue.popleft() # Efficiently removes from the left (front)
print(f"Dequeued item: {dequeued_item}")
print(f"Queue after dequeuing: {queue}")