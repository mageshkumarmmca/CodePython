productbrands = ['Iphone', 'Samsung', 'LG', 'Song']
new_dic = dict.fromkeys(productbrands, [])
new_dic['Iphone'].append(1)
# {'Iphone': [1], 'Samsung': [1], 'LG': [1], 'Song': [1]}'
print(new_dic)

d = {key: [] for key in productbrands}
d['Iphone'].append(1)
# {'Iphone': [1], 'Samsung': [], 'LG': [], 'Song': []}
print(d)

# Nested Array
nested = [[1, 2], [2, 3], [4, 5], [6, 9, 6, 88, 1]]

flat = [x for sub in nested for x in sub]
print(flat)

even = [x for sub in nested for x in sub if x % 2 == 0]

print(even)

odd = [x for sub in nested for x in sub if x % 2 != 0]
print(odd)
