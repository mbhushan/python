import string

def is_palindrome(text):
    #convert the string to lower case and strip left and right spaces
    text = text.lower().strip()

    #create a exclusion set of all punctuations
    exclude = set(string.punctuation)

    '''create a new string which has all the characters from the text which
    not in punctuation set '''
    text = ''.join(ch for ch in text if ch not in exclude)

    #replace space with empty
    text = text.replace(" ", "")

    #check if the text and its reverse are same ie if they are palindrome :)
    return text == text[::-1]

text = raw_input("Enter text: ")

if is_palindrome(text):
    print 'PALINDROME!!'
else:
    print 'NOT PALINDROME!!'
