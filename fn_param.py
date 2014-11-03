
def find_max(a, b):
    if a == b:
        print 'Both are equal!'
    elif a > b:
        print '{} is greater than {}'.format(a,b)
    else:
        print '{} is greater than {}'.format(b,a)

x = int(raw_input("Enter first number:" ))
y = int(raw_input("Enter second number: "))

find_max(x,y)
