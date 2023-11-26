

def checkID(ID):
    if not ID.isnumeric(): # ID must all be numbers
        return False
    
    if len(ID) != 11: #ID must be 11 digits
        return False
    
    if int(ID[0]) == 0: #The first number of the ID can't be 0
        return False

    sum1 = int(ID[0]) + int(ID[2]) +int(ID[4]) +int(ID[6]) +int(ID[8])
    sum2 = int(ID[1]) + int(ID[3]) +int(ID[5]) +int(ID[7])

    if (sum1*7 - sum2)%10 != int(ID[9]): #For a valid ID result will be equal to the 10th digit
        return False
    
    sum3 = sum1 + sum2 + int(ID[9]) 

    if sum3%10 != int(ID[10]): #For a valid ID result will be equal to the 11th digit
        return False
    
    return True


ID = "placeholder"
print(checkID(ID))