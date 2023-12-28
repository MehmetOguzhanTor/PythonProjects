def form(file_read):
    '''
    form function  reads the words and their positions from the
    file into two parallel lists words and numbers and then forms a sentence
    by concatenating the words in the words list according their positions in
    numbers list in ascending order.
    
    number is an integer to get the number part of the line in the text
    pop is string to get the str part of the line in the text
    words and numbers are empty lists for words and numbers separately from the text
    out_text is an empty string to write the sentence in the corrent form 
    
    The function returns out_text string as an output that will be displayed outside
    '''
    words = []
    numbers = []
    out_text = ''

    ##looking every line of the file and 
    for line in file_read:
    
        number = int(line[-2])
        numbers.append(number)
        pop=str(line[:len(line)-3])
        words.append(pop)

    for i in range (1, len(numbers)+1):
        place = numbers.index(i)
        out_text += words[place] + ' '
    return out_text

def main():
    ## Reading the words.txt file 
    file_read = open('words.txt', 'r')
    ##calling function form and displayin the sentece in the corrent form
    print(form(file_read))
    ##closing the file
    file_read.close()

if __name__ == "__main__":
  main()



