def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse_text(text)

input = raw_input("Enter string: ")

if (is_palindrome(input)):
    print 'Yes, its a palindrome!'
else:
    print 'No, its not a palindrome!'
