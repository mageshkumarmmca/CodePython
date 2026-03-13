def high_and_low(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    return (highest,lowest)

numbers = [5,8,4,6,9]
(highest, lowest) = high_and_low(numbers)
print(highest)
print(lowest)