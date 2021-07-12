#Leah Oswald
#2420610
#Collaboration: none

#Program that uses functions to convert temperature units.
#Get temperature from user.
#Get unit from user.
#Display results.

#import module temps.py 
import temps

#define program main
def main():
    #prompt user to a temperature
    temperature = float(input('Enter a temperature: '))
    #prompt user for the unit of measure
    unit = input('Was that input Fahrenheit or Celsius (enter c or f): ')
    #determine if the unit is celsius
    if unit == "c":
        #use function c_to_f from temps.py
        temps.c_to_f(temperature)
    #if unit is not celsius use function f_to_c from temps.py and assign to variable celsius  
    else:
        celsius = temps.f_to_c(temperature)
        #display results
        print(temperature, 'Fahrenheit equals', format(celsius, '.3f'), 'Celsius')




#run program
main()
