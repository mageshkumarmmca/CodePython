# Explanation
# 1. Set iteration order is not guaranteed and may appear stable in small examples but is not reliable.
# Even if printing obj looks like the elements are "in order," remember this is an incidental effect of the internal hash state and Python implementation details. With more operations or in different Python versions, the order or which element pop() removes may differ.
#
# 2. set.pop() removes an arbitrary element
# This means:
#
# You cannot predict which element will be removed.
# The observed removed element might look like the "first inserted" or "smallest" element in some runs, but it's just coincidence.
# The element removed is the one at the lowest internal hash bucket found (implementation detail).
# 3. Example output you might observe (note: your actual output may vary)
# Actual Set object list : {0, 1, 2, 3, 4}
# After pop executed 1 : {1, 2, 3, 4}
# After pop executed 2 : {2, 3, 4}
# Here pop() removed 0 first, then 1, but this pattern is not guaranteed.
#
# How to get predictable behavior?
# If you want to remove an element predictably from a collection with unique elements:
#
# Use a list or collections.deque if order matters.
# Use sorted() or min() / max() on the set before removing:
# python
#
# obj = {3, 0, 2, 4, 1}
#
# # Remove the smallest element reliably:
# smallest = min(obj)
# obj.remove(smallest)
#
# print(obj)
# Or convert to a list for ordered removals:
# python
#
# obj = {3, 0, 2, 4, 1}
# lst = sorted(obj)  # [0, 1, 2, 3, 4]
# first_element = lst[0]
#
# obj.remove(first_element)
# print(obj)
# Summary
# Your output and the order you observe is not guaranteed by Python.
# set.pop() removes an arbitrary element, so you should not rely on the order or which element it removes.
# To remove elements in a specific order, use an ordered structure or explicitly pick elements (e.g., with min, max, or converting to a list).

obj = set()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(4)
obj.add(1)
obj.add(4)
obj.add(1)

print('Actual Set object list :', obj)
obj.pop()

print('After pop executed 1 :', obj)
obj.pop()
print('After pop executed 2 :', obj)
print(obj)

lists = [1, 4, 2, 4, 5, 6, 3, 6]
print('pop invoked using lists :', lists.pop())
print('After pop executed 1 :', lists)
