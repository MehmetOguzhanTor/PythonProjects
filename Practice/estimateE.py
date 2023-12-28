import math
def estimateE(value):
    '''    
    This function takes an integer value as input and
    calculates each element of the following series and returns a tuple holding the
    desired values

    sec_value which is an int at the beginning is for calculation of factor
    tuple_dis is a tuple that will contain the output
    total is an int that shows the total of calculated values
    error is an int that will show the error between real e and calculated e
    
    Returns:
        the function returns tuple_dis that is the tuple of all calculated values in the formula
    '''
    sec_value = 1
    tuple_dis = (+1,)
    total = 0
    error = 0
    
    if value == 0:
        tuple_dis = (+1,)
    else:
        for i in range (0, value+1):
            if i ==0:
                sec_value = +1
            else:
                for x in range (1, i+1):
                    sec_value = sec_value*x

                sec_value = 1/sec_value
                tuple_dis += (sec_value,)
            sec_value=1
    print('E = ', end = '')
    for b in tuple_dis:
        print(' +', b, end = '')
        total += b
    
    print ('\n' + 'Estimated Value: ', total)
    error = math.exp(1) - total
    print('Error = ', error)
    return tuple_dis

def main():
    ##Taking the input of n from the user which will be an integer
    value = int(input('Enter the value of n: '))
    ## Calling the function for calculations
    estimateE(value)

if __name__ == "__main__":
  main()
