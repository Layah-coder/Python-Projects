#Leah Oswald
#SPC ID# 2420610

#collaboration: none.

#This program prompts the user for cost and quantity of an item.
#Then diplays the subtotal.

def main ():
    #prompt user for item cost and assign to variable unit_cost
    unit_cost = float(input('Enter the unit price: '))
    #prompt user for item quantity and assign to variable quantity
    quantity = int(input('Enter the quantity: '))
    #calculate the total and assign to the variable subtotal
    subtotal = unit_cost * quantity
    #formating subtotal 2 decimal places and outputing the results
    print('Please pay $', format(subtotal, '.2f'), sep='')

main ()
