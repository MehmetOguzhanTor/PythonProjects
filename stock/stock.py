
"""
Mehmet Oguzhan TOR
21301554
4/12/2020
CS 115 - 2
"""
'''
The stock class stores name, count, price and city of a data in private
It has an init() method that takes the values of all four attributes as parameters
The class has get method for all of the attributes but only count has a set method
The class returns the attributes in a desired order

'''
class stock:
    def __init__(self, name, count, price, city):
        self.__name = name
        self.__count = count
        self.__price = price
        self.__city= city
    
    def getname(self):
        return self.__name
    
    def getcount(self):
        return self.__count
    
    def setcount(self, count):
        self.__count = count
        
    def getprice(self):
        return self.__price
            
    def getcity(self):
        return self.__city
    
    def __str__(self):
        return 'Name: {} \nCount: {} \nPrice: {} \nCity: {}'.format(self.__name,self.__count, self.__price, self.__city)
    
    def __repr__(self):
        return 'Name: {} \nCount: {} \nPrice: {} \nCity: {}'.format(self.__name,self.__count, self.__price, self.__city)
    
    

    
def getByStockQuantity(stocks, quantity):
    '''
    getByStockQuantity method : takes a list of stocks and a quantity as
    parameters returns the list of Stocks in the database who have a quantity greater than
    that passed as a parameter

    Parameters
    stocks : lists of stocks
    quantity : int, desired quantity

    Returns 
    -------
    L_stocks : list that has a quantity greater than parameter
    
    '''
    L_stocks = []
    for i in stocks:
        if int(i[1]) > quantity:
            L_stocks.append(i)
    return L_stocks

def getByPrice(stocks, price):
    '''
    getByPrice method returns the list of Stocks in the database who have a
    price less than the value passed as a parameter.

    Parameters
    ----------
    stocks : Lists of stocks
    price : float, desired price

    Returns
    -------
    L_stocks : List of stocks that has less value than the parameter.

    '''
    L_stocks = []
    for i in stocks:
        if float(i[2]) < price:
            L_stocks.append(i)
    return L_stocks

#Reading the text file
open_file = open('input.txt', 'r')
#empty list
return_stocks =[]

#appending the information into the empty list
for i in open_file:
    add_line = i.strip('\n')
    add_line = add_line.split(';')
    return_stocks.append(add_line)

##Using the methods
quantity = getByStockQuantity(return_stocks,6)
price = getByPrice(quantity,5)

##Printing the result
print('Printing Stocks whose price is less than 5 and count is over 6: ')
for stck in price:
    new_stock = stock(stck[0], int(stck[1]), float(stck[2]), stck[3])
    print(new_stock)
    print()


    