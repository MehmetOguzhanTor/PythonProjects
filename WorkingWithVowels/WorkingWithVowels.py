"""
The is_vowel() function tkaes a string and returns True if this string is a single vowel character,
False otherwise

Parameters:
vowel_chars is a string given for the clearification of all of the vowel characters in the alphabet
cr is the string input of the function
Returns:
The program returns bloolean       

"""
def is_vowel(cr):
    vowel_chars = 'aeiou'
    return cr in vowel_chars


"""
The count_vowels() takes a string and counts and returns the number of vowels in
this string using the is_vowel() function 

Parameters:
integer number is for spesifiying the range of the input given by the user to help in while loop
integer count is for counting the vowels inside the input
word is the string input of the function
Returns:
The program the integer count as it shows the number of vowels in the input     

"""
def count_vowels(word):
    number = 0
    count = 0
    while number < len(word):
        if is_vowel(word[number]):
            count += 1
        number += 1
    return count    

"""
The all_vowels() takes a string and checks if all vowels exist in this string or not.
The function will return True if all exist, otherwise False will be returned.


Parameters:
vowel_chars is a string given for the clearification of all of the vowel characters in the alphabet
all_vowel is the bloolean that will give us if the all vowels exist in the input
text is the string input of the function
Returns:
The program prints the massage if all vowels exist in the input  

"""
def all_vowels(text):
    vowel_chars = 'aeiou'
    all_vowel = True
    for i in vowel_chars:
        if i not in text:
            all_vowel = False
    if all_vowel:
        print('All Vowels exist in the given string')
    
               
"""
The display_which_vowels()  takes a string and displays which vowels exist in the
string.

Parameters:
vowel_chars is a string given for the clearification of all of the vowel characters in the alphabet
text is the string input of the function

Returns:
The program prints every time of of the vowel chars exist in the input   

"""   
def display_which_vowels(text):
    vowel_chars = 'aeiou'
    for i in vowel_chars:
        if i in text:
            print('"' + i + '" exists in "' + text + '"')



"""
The capitalize_vowels()  takes a string and creates a new string by capitalizing the
vowels in the given string.

Parameters:
string output is to return the new string
text is the string input of the function

Returns:
The program return the new output that is the new string with capitalized the vowels   

"""
def capitalize_vowels(text):
    output = ''
    for i in text:
        if is_vowel(i):
           output += i.upper()
        else:
            output += i
    return output



##Getting the input string from the user
user_says = str(input('Enter a string:'))

## Using all of the function to get desired outcomes
print('There are', count_vowels(user_says), 'number of vowels')

all_vowels(user_says)

display_which_vowels(user_says)

print('New String: ' + capitalize_vowels(user_says))


