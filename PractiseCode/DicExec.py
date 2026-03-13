hashTable = {"Magesh": "8123577656", "Dhanvith": "98123576654", "Chervik": "847976163"}
mag_phone = hashTable['Magesh']
print('Magesh phone num is : {}'.format(mag_phone))

hashTable['Gowthami'] = '8662102563'
print(hashTable)
print(len(hashTable))

# If the key is existing or contains check

if 'Magesh' in hashTable.keys():
    print('Key found in map')

# Delete statement to remove the element from the list.
del hashTable['Magesh']
print(hashTable)

for value in hashTable.values():
    print(value)