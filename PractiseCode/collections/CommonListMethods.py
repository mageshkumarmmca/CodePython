names = ["magesh", "kumar", "dhanvith", "chervik"]

names.append("gowthami")
names.extend(["mani", "mano"])
names.insert(0, "muniyappa")

print(names)
# Find the index where the "chervik" positioned
print(names.index("chervik"))
# Find the count how my occurrence of name "magesh" in the list.
print(names.count("magesh"))

# Remove the last name from the List
popped = names.pop()
print(popped)
print(names)

# Sort the names
names.sort()
print(names)

# Print the name in reverse order
names.reverse()
print(names)

# copy the original object into new obj.
employees = names.copy()
print(employees)
