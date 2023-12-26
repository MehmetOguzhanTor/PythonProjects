'''
The yourname_doc script  calls pluralizeAllWords
function to luralize the words in ‘wordList.txt’ and create a new file for the successfully pluralized
words as ‘pluralWordList.txt.
'''
##importin the doc_module script that contains the functions
import doc_module
##reading, writing and openning the files that are necessary
file_read = open('wordList.txt', 'r')
file_write = open('‘pluralWordList.txt', 'w')
file_append = open('‘pluralWordList.txt', 'a')

##Calling the pluralizeAllWords function from doc_module script
doc_module.pluralizeAllWords(file_read, file_write,file_append)

##closing all of the files
file_read.close()
file_write.close()
file_append.close()