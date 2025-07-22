queue = []
# Enqueue (add elements)
queue.append('A')
queue.append('B')
queue.append('C')
print(f"Queue after enqueuing: {queue}")
# Dequeue (remove element from the front)
dequeued_item = queue.pop(0)
print(f"Dequeued item: {dequeued_item}")
print(f"Queue after dequeuing: {queue}")

# Peek (view the front element without removing)
if queue:
    front_item = queue[0]
    print(f"Front item (peek): {front_item}")
# Check if empty
is_empty = not bool(queue)
print(f"Is queue empty? {is_empty}")

# Get size
size = len(queue)
print(f"Queue size: {size}")