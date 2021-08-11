#-----------------------------------------------------------------
#  IT109_122.py  - challenge/review problem for class:
#                      open/read books.txt file into list
#                      prompt for file name
#                      split into description and price using ','
#
#  Input: books.txt
#
#  By Gene Shuman, 11/11/2018     (original:  #054, 04/14/2018)
#------------------------------------------------------------------

# Prompt for file name

infile = input('Please enter fully qualified file name for books items: ')
fi = open(infile,"r")
booksIn = fi.readlines()    # read all lines into presList

input('\n1. "Enter" to see ' + str(infile) + ' printed as a list: \n')
print(booksIn)

input('\n2 "Enter" to apply strip and split, then print line by line \n')
bookList = [ ]
for b in booksIn:            # create item list from comma-separated...
    if len(b) > 4:           #  ...data = description + price
        x = b.split(',')
        x[0] = x[0].strip()
        x[1] = float(x[1].strip())
        bookList.append(x)

for b in bookList:
    print(b[0], b[1])

# Always close the file 
fi.close()
 
