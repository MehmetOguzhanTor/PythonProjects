'''
This module contains 3 function that are used in the yourname_doc program 
'''

def isAllLetter(text):
    '''    
    Checks wheter the text consist of all letters or not. The function does that by using a for loop and isalpha()

    check : boolean parameter to that checks every i in the text
    
    returns:
        check which is boolean of isAllLetter
    '''
    check = True
    for i in text:
        if not i.isalpha():
            check = False
    return check


def pluralizeWord(word):
    '''    
    The function pluralizes the word by looking its last character

    wordOut: an empty string that the new word is writen into
    
    returns:
           wordOut string which is the pluralized word
    '''
    wordOut = ''
    if word[-1] == 'y':
       wordOut = word[:-1] + 'ies'
    else:
        wordOut = word + 's'
    return wordOut 
    
   

def pluralizeAllWords(file_read, file_write,file_append):
    '''    
    The function pluralizes all words that are consists of only letters
    The words are read from the file_read and writen into file_write as pluralized
    The function writes the percentage of the pluralized word into the same file with file_append

    wordCount : integer that counts the number of words in the file
    pluralCount: integer that count the pluralized words that are writen into outout file
    pluralPercentage: float that inculudes the percentage of the pluralized words
    
    returns:
           The function returns none since the write and append functions are done inside
    '''
    wordCount = 0
    pluralCount = 0
    
    for line in file_read:
        wordCount += 1
        if isAllLetter(line[:-1]):
##          print(pluralizeWord(line[:-1]))
            file_write.write(pluralizeWord(line[:-1]) +'\n')
            pluralCount += 1
    pluralPercentage = pluralCount/wordCount*100
##  print('{0:.2f}'.format(pluralPercentage)+'%')
    file_append.write('{0:.2f}'.format(pluralPercentage)+'% of the words are pluralized')
 
            
            
