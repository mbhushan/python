class ShortInputException(Exception):
    '''A user defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = raw_input("Enter something: ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print 'Why did you do an EOF error on me!'
except ShortInputException as ex:
    print ('ShortInputException: the input was {0}, expected was atleast {1} \
           ').format(ex.length, ex.atleast)
else:
    print 'NO EXCEPTION WAS RAISED!'

