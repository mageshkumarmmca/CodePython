names = ('Magesh', 'Kumar', 'Rajesh', 'Mohan', 'Shiva')

for name in names:
    print(name)

list_names = list(names)

print('Type of object is : {}'.format(type(names)))
print('Type of object is : {}'.format(type(list_names)))

# Assign multiple variable to tuple

(mag, kum, raj, moh, shiv) = names
print(mag)
print(kum)



