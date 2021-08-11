#----------------------------------------------------------------
# IT109_A8_itemMenu.py  - Stand-alone 'itMenu' function
#
# Shows several techniques and advantages of creating a function:
#     (1) Reduces amount of code - write once/use many times
#     (2) Dynamic build of a menu using an input list
#     (3) encapsulation - only uses parameters, no 'global' refs.
#     (4) displays menu for all item categories, not just 'books'
#     (5) includes a docstring stating what the function does and
#         how to use it
#
# Provided to IT109 class as a good model for a function and
# for use in A9 if needed.
#
# Gene Shuman   11/19/2018
#----------------------------------------------------------------
# Mods
# 
#----------------------------------------------------------------

# Note: students using this function only need to cut/paste the code
# below.  No need to include the above comments

import os # include this import only if not done elsewhere in your code

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

# Only cut/past the above code.  The code below does a basic demo of using
# the above function.  There is no reason to include it in your code.

category_menu = """\n\n
             Select an item from the following menu or checkout:
             
               1 = Books 
               2 = electronics
               3 = clothing
               d = show cart contents
               c = checkout
        
        """

# category items tuples - one per category --------------------------------

book_list  =  (('Origin', 19.95),
               ('Grant', 22.50),
               ('Prairie Fires', 18.95),
               ('The Elements of Style', 11.25),
               ('Animal Farm', 9.95),
               ('Slaughterhouse Five', 7.50),
               ('Python Programming', 24.50))
elect_list  = (('HP Laptop', 429.50),
               ('EyePhone 10', 790.00),
               ('Bose 20 Speakers', 220.00),
               ('TP-Link Router', 19.95))
cloth_list  = (('T-shirt', 9.50),
               ('Shoes', 45.00),
               ('Pants', 24.00),
               ('New Balance Shoes', 79.95),
               ('North Face Jacket', 169.50))

# start of active code*********************************

category = 1

while category not in ('x', 'c'):
    os.system('cls')
    print (category_menu)
    category = input('Select category (1 - 3), d, or x :')
    if category == '1':
        item_pic = itemMenu('Books', book_list)
    elif category == '2':
        item_pic = itemMenu('Electronics', elect_list)
    elif category == '3':
        item_pic == itemMenu ('clothing', cloth_list)
    print ('Item# ', item_pic, ' selected.')
input ('\nHit "Enter" to end demo ')
           
