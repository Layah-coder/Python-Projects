# Leah Oswald
# 2420610
# Collaboration: none

#program that calculates a salesperson's total sales and pay.
#prompt user to enter type of vehicle and assign to variable vehicle1.
#prompt user to enter selling price of vehicle1 and assign to selling_price.
#prompt user to enter type of vehicle and assign to variable vehicle2.
#prompt user to enter selling price of vehicle2 and assign to variable selling_price2.
#calculate total sales and pay
#display results

def main ():
#get user input
    vehicle1 = input('Did you sell a new  or used vehicle? Enter New or Used (Case sensitive): ')
    selling_price = float(input('Enter vehicle price: '))
#decide commission1
    if vehicle1 == 'New':
        commission1 = 1800
    else:
        commission1 = selling_price * .1
#get user input     
    vehicle2 = input('Did you sell a new  or used vehicle? Enter New or Used (Case sensitive): ')
    selling_price2 = float(input('Enter vehicle price: '))
#decide commission2
    if vehicle2 == 'New':
        commission2 = 1800
    else:
        commission2 = selling_price2 * .1
#calculate total price of both vehicles
    total_sales = selling_price + selling_price2
#calculate total pay for salesperson
    total_pay = commission1 + commission2
#display results
    print('Total sales $', format(total_sales, ',.2f'), sep='')
    print('Total pay $', format(total_pay, ',.2f'), sep='')
main ()
