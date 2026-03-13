def printStr():
    print('Welcome to Python Function')

def welmsg(firstName, lastName):
    print('Hi {1}, {0}'.format(firstName, lastName))
    print('Diff {}, {}'.format(firstName, lastName))

def hostconnect(hostname, port='8080'):
    print('Connecting to HostName : {} Port :{}'.format(hostname,port))

def findOddOrEven(input):
    if input%2 == 0:
        return 'Even Number'
    else:
        return 'Odd Number'


printStr()
welmsg('Magesh','Kumar')
welmsg(firstName='Raj', lastName='kumar')
hostconnect('mkgroup.com')
print('Output :',findOddOrEven(5))

