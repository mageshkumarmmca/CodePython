squares = [x * x for x in range(6)]
print(squares)

evenNum = [x + x for x in range(1, 10)]
print(evenNum)

fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)

fab = [(x + 1) + x for x in range(1, 5)]
print(fab)

# nested (flatten a 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(flat)
