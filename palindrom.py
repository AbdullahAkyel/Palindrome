text = input('İnput text : \n')
# we get a text from the user
reverse =text[::-1]
# we reverse the text

print('İnput text = %s' % (text))
print('Reverse input text = %s' % (reverse))

if reverse == text:
    print('This text is palindrome')
else:
    print('This text is not palindrome!')