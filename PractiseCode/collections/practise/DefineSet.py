# The most common and efficient way to create a set is by placing comma-separated values inside curly braces {}
names = {"magesh", "kumar", "dhanvith", "gowthu", "kumar"}
print(names)

# Mixed Data type set
empDetail = {"Magesh", 30, "Bangalore", 560311, True, 155220.50}
print(empDetail)

# . Using Set Comprehensions
# Create a set of squares for numbers 0-4
squares = {x ** 2 for x in range(5)}  # Result: {0, 1, 4, 9, 16}

even = []
evenset = set()

for x in range(10):
    if x % 2 == 0:
        even.append(x)  # Updates your list: [0, 2, 4, 6, 8]
        evenset.add(x + 1)  # Updates your set: {1, 3, 5, 7, 9}
print('even numbers :', even)
print('even set', evenset)
# Filtering items (e.g., only even numbers)
evens = {n for n in range(10) if n % 2 == 0}


print('Even Numbers :',evens)
