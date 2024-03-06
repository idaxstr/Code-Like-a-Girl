print('Welcome to the palindrome checker!')
word = input('Enter sentence or word: ')
#make user input lower case and delete the spaces. I have decided to do this in a seperate line, so the final print will have the actual word typed by user. 
word_lower = word.lower().replace(" ", "")
#turn string into list
word_list = list(word_lower)
#reverse the list
word_list.reverse()
#turn the list back into a string
new_word = ''.join(word_list)
#compare the two strings to see if they are the same
if (word_lower == new_word):
    print (f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
