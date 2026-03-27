number = [4, 5, 2, 5, 4, 2, 5, 5, 4, 7, 8]

# remove duplicate and sorted values
unique2 = list(set(number))
print(unique2)

# dict.fromkeys is Preserves Order
unique1 = list(dict.fromkeys(number))
print(unique1)

# Using a Loop or List Comprehension
unique = []
for x in number:
    if x not in unique:
        unique.append(x)
print(unique)

# comprehension is a shorthand way to create a new collection (like a list, dictionary, or set) from an existing one
# in a single line of code.

# List Comprehension
seen = set()
unique = [x for x in number if not (x in seen or seen.add(x))]
