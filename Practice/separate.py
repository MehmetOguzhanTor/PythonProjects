def separate(original_list):
    '''
    The function separate gets a list of mixed types and returns a
    dictionary of each different type as keys and the list of elements of that type as a
    value.
    
    Parameters
    
    int_list, float_list, bool_list and str_list are emty list to store the elemets that are in
    4 different types

    Returns
    The function returns the created dictionary of separeted typed elemets in 4 different lists
    

    '''
    int_list = []
    float_list = []
    bool_list =[]
    str_list = []

    for i in original_list:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == float:
            float_list.append(i)
        elif type(i) == bool:
            bool_list.append(i)
        else:
            str_list.append(i)
    type_dic = {'int' : int_list, 'float' : float_list, 'bool' : bool_list, 'str' : str_list}

    return type_dic

def main():
    ## The original list    
    list_original =  [2, 3.75, False, 'Today', 'CS115', 6, 1.5, 4.0, 'python', True, 25, 1.9]

    ## Printing the original list first
    print('Original List = ', list_original, '\n')

    ## calling the separate funciton to get the dictionary of original list
    dict_out = separate(list_original)

    ##Displayin all of the elements that are in different lists one by one
    for key in dict_out: 
        print('<class ' + key + '> -> ',dict_out[key])

if __name__ == "__main__":
  main()
