def max (x, y):
    '''finds the max interger out of the two inputs
    and prints the maximum ones'''
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print 'Both are EQUAL!!!'

x = int(raw_input('Enter x: '))
y = int(raw_input('Enter y: '))

ans = max (x, y)

print 'Max is: ', ans
print max.__doc__

