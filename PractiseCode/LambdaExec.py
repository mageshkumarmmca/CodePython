
x = lambda a, b : a +' '+ b

print(x('magesh','kumar'))

for n in range(1,6):
    print(n)

def recursions(n):
    if n<=0:
        print('Done')
    else:
        print(n)
        recursions(n-1)

recursions(5)

n = 5
f = 1

for i in range(1, n+1):
    f *= i

print(f)


def factorial(f, n):
    s = 1
    for i in range(f, n + 1):
        s *= i
    return s


print(factorial(1, 5))

x = input('Enter value:')


def calculate(str):
    upperChar = []
    lowerChar = []
    for n in str:
        if n.isupper():
            upperChar.append(n)
        elif n.islower():
            lowerChar.append(n)
    print('No. of uppercase', len(upperChar))
    print('No. of lowercase', len(lowerChar))


print(calculate(x))



