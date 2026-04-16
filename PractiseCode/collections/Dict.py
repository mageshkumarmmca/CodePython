names = ['Magesh', 'Kumar', 'Dhanvith', 'Gowthami', 'Magesh', 'Kumar']
# Find the string count using comprehension code
nameLenmap = {n: len(n) for n in names}
print('Using comprehension -> ', nameLenmap)

from collections import Counter

# Using Dict reference
counts = dict(Counter(names))
print('Using Collection -> ', counts)

# Using Comprehension code
countdict = {name: names.count(name) for name in names}
print('Using Dict coding -> ', countdict)

counts = {}
for name in names:
    counts[name] = counts.get(name, 0) + 1

print('For loop coding -> ', counts)
