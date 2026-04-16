# Stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # 3

# Queue (FIFO) - use deque for efficiency
from collections import deque
q = deque()
q.append("a")
q.append("b")
print(q.popleft())  # a