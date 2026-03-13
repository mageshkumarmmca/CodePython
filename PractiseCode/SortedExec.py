names = ['Magesh', 'Dhanvith', 'Chervik', 'Gowthami']

sorted_animals = sorted(names)

print('Actual list   :{}'.format(names))
print('Using Sort Fun :{}'.format(sorted_animals))
names.sort()
print('Using inbuilt sort fun: {}',names)

new_names = ['Rajesh','Kumar']

consolidated = names + new_names

print('Consolidated Name :{}'.format(consolidated))