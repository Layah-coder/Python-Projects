# Leah Oswald
# 2420610
# Collaboaration: none

# Program that reads invetory file for Chica Chic.
# Open inventory file for reading.
# Assign lines from file to variables.
# Calculate cost of items in stock and total inventory value.
# Close file.
# Display results to user.


def main():
    #open file for reading
    file = open('inven.txt', 'r')
    #assign value for accumulator
    value = 0
    print('Chica Chic Inventory', '\n')
    #prime read for loop
    line = file.readline()
    #continue reading lines till lines are blank
    while line != '':
        #remove \n on the right and assign item
        item = line.rstrip('\n')        
        #read item price, convert to float, and assign to variable price
        price = float(file.readline())
        #read stock quantity, convert to int, and assign to variable stock
        stock = int(file.readline())
        #calculate total cost of one item in inventory
        cost = stock * price
        #accumulator cauculates total cost of all items in inventory
        value += cost
        #display results of inventory with format
        print(item, ', $', format(price, ',.2f'), ' each, ', stock, ' in stock, ', 'value $', format(cost, ',.2f'), sep = '')
        #check if more items are in inven.txt file
        line = file.readline()
    
    #close file    
    file.close()
    #notify user that the file has ended
    print('End of file')
    #display the total value of all items in inventory
    print('Total inventory value $', format(value, ',.2f'), sep = '')

main()
