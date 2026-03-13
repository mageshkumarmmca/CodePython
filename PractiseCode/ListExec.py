

name = ['Magesh','Dhanvith','Chervik','Gowthami']
name.append('kumar')

add_new = ['Raj','Siva','Ganesha']
name.extend(add_new)

name.insert(2,'Rajesh')
print('First name : {}'.format(name[0]))
print('Second name : {}'.format(name[2]))
print('Last name : {}'.format(name[-1]))