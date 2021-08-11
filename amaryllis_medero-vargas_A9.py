# Program name: amaryllis_medero-vargas_A9.py A9 – On-line Order Shopping Cart (Part 3 of 3) Author: Amaryllis Medero-Vargas
"""
    function to read files and turn them into lists
    no paramters 
    returns list of items
"""
def filetolist():
    newlist = []
    while True:
        try:
            filename = input("Enter file name to be used: ")
            fi = open(filename, "r")
        except IOError:
            print("IO Error: file not found")
            continue
        else:
            filein = fi.readlines()
            fi.close()
            for i in filein:
                if len(i) > 4:
                    x = i.split(',')
                    x[0] = x[0].strip()
                    x[1] = float(x[1].strip())
                    newlist.append(x)    
            return newlist
"""
#   function to display cart
#   1 parameter: currentcart is list of items that is displayed
"""
def displaycart(currentcart = []):
    print("\n\t\t\t{0:26s}{1:8s}{2:8s}".format("Item Description" , "Price" , "Quantity"))
    print("\n\t\t\t{0:26s}{1:8s}{2:8s}".format("===========================",'========','========'))
    for n in range(len(currentcart)):
        print("\n\t\t\t{0:26s} ${1:8.2f}{2:8d}".format(currentcart[n][0],currentcart[n][1], currentcart[n][2]))
    input("\nPress Enter to continue:")
    
    """
#   function for checking out
#   5 parameters
#       grandtotal: to be filled; totals are added into here; is returned
#       onecart: singular list of items
#       carts: list of carts
#       report: holds total of each category
#       total: totals of each category filled into here
"""
def checkout(grandtotal, onecart = [], carts = [], report = [], total = []):
    print("\n\t\t\tcost of items\t\tnumber of items\n")
    
    total[1] = total[1] + report[0][1] + report[1][1] + report[2][1]
    total[2] = total[2] + report[0][2] + report[1][2] + report[2][2]
    print(total[0], '\t\t\t${0:10.2f}'.format(total[1]), '\t\t\t',total[2])
    grandtotal[1] = grandtotal[1] + total[1]
    grandtotal[2] = grandtotal[2] + total[2]
    carts.append(onecart)
    return grandtotal
    
"""   
# function displaying menu items from item list
# copied from IT109_122.py
# author: Gene Shuman
"""
def itemMenu (category, itemList):
    """itemMenu function - displays menu of variable number of shopping items.
       Inputs: category (books, etc.), list of item descriptions and prices.
       Returns: selected menu item (integer, 1 to n), d, or x
       ---------------------------------------------------------------------"""  
    os.system('cls')
    print ('\n\n\t\t ' + category + ' menu')
    print ('\n\t\t Select from the following items, display cart, or checkout: ')
    print('\n\t\t\t {0:3s}  {1:26s}  {2:8s}'.format('No.', 'Item Description', 'Price '))
    print('\t\t\t {0:3s}  {1:26s} {2:8s}'
          .format('===', '===========================', '========'))
    for n in range(0, len(itemList)):
        print('\t\t\t {0:>2s} - {1:26s}  ${2:8.2f}'.format(str(n+1), itemList[n][0], itemList [n][1]))
    print('\n\t\t\t {0:>2s} - {1:26s} '.format('d',  'display cart contents '))
    print('\t\t\t {0:>2s} - {1:26s} '.format('x', 'return to category menu '))
    menuPic = input('\n\nEnter Selection (1 to {0:>2s}, "d", or "x"): '.format(str(len(itemList))))
    return menuPic
"""
   function to add into and check cart list for redundancy
   5 parameters
       category: used for report
       menupic: used for item and price; param for lst
       lst: list of items from file; used for item and price
       currentcart: chosen item is put into this list
       report: list for later use in check out
"""
def enhance2(category, menupic, lst = [], currentcart = [], report = []):
    categnum = ast.literal_eval(category) - 1
    menunum = ast.literal_eval(menupic)
    item = lst[menunum-1][0]
    price = lst[menunum-1][1]
    amt = 1
    placeholder = [item, price, amt]
    
    if len(currentcart) == 0:
        currentcart.append(placeholder)
    else:
        for n in range(len(currentcart)):
            if placeholder[0] == currentcart[n][0]:
                currentcart[n][1] = currentcart[n][1] + price
                currentcart[n][2] = currentcart[n][2] + amt
            elif placeholder[0] != currentcart[n][0] and n == len(currentcart)-1:
                currentcart.append(placeholder)
            
    report[categnum][1] = report[categnum][1] + price
    report[categnum][2] = report[categnum][2] + 1
                
            

# main
import os #used for clearing screen os.system('cls')
import ast #parsing
import datetime #used for date/time stamps datetime.datetime.now( ).__str__( )
booklist = []           #books.txt
clothlist = []          #clothing.txt
eleclist = []           #electronics.txt
cartlist = []
categmenu = """Select one of the categories or checkout:
    1 - Books
    2 - Clothing
    3 - Electronics
    d - Cart Contents
    c - Checkout"""
grandtotal = ['Grand Total:', 0.00, 0]


booklist = filetolist()
clothlist = filetolist()
eleclist = filetolist()

yorn = ""
while yorn != "n" and yorn != "N":
    cartreport = [
          ['Books', 0.00, 0],
          ['Electronics', 0.00, 0],
          ['Clothing', 0.00, 0]]
    total = ['Total:', 0.00, 0]
    categ = ""
    cart = []
    while categ not in ('c', 'C'):
        subcateg = ""
        os.system('cls')
        print(categmenu)
        categ = input("Select one of the categories or checkout (1 – 3, 'd', or ‘c’): ")
        while categ not in ("1",'2','3','d','D','c','C'):
            categ = input("Wrong input! Select one of the categories or checkout (1 – 3, 'd', or ‘c’): ")
        if categ == "1":
            while subcateg not in ("x" ,"X"):
                subcateg = itemMenu("Books", booklist)
                try:
                    enhance2(categ, subcateg, booklist, cart, cartreport)
                    
                except ValueError:
                    if subcateg not in ("x","X","d","D"):
                        print("Wrong input!")
                    elif subcateg == "d" or subcateg == "D":
                        displaycart(cart)
        elif categ == "2":
            while subcateg not in ("x" ,"X"):
                subcateg = itemMenu("Clothing", clothlist)
                try:
                    enhance2(categ, subcateg, clothlist, cart, cartreport)
                except ValueError:
                    if subcateg not in ("x","X","d","D"):
                        print("Wrong input!")
                    elif subcateg == "d" or subcateg == "D":
                        displaycart(cart)
        elif categ == "3":
            while subcateg not in ("x" ,"X"):
                subcateg = itemMenu("Electronics", eleclist)
                try:
                    enhance2(categ, subcateg, eleclist, cart, cartreport)
                except ValueError:
                    if subcateg not in ("x","X","d","D"):
                        print("Wrong input!")
                    elif subcateg == "d" or subcateg == "D":
                        displaycart(cart)
        elif categ == "d" or categ == "D":
            displaycart(cart)
        else:
            print("\nSummary of shopping cart: ")
            displaycart(cart)
            grandtotal = checkout(grandtotal, cart, cartlist, cartreport, total)
            
            
            yorn = input("Are there more carts to be processed? Enter 'Y' or 'N': ")
            while yorn != "Y" and yorn != "y" and yorn != "N" and yorn != "n":
                yorn = input("Wrong input! Are there more carts to be processed? Enter 'Y' or 'N': ")
                
print("Total number of carts: ", len(cartlist))
print("Total cost of items: ${0:8.2f}".format(grandtotal[1]))
print("Total number of items:", grandtotal[2])

input("\n\nHit Enter to end program")
