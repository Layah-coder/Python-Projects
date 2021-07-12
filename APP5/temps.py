#Leah Oswald
#2420610
#collaboration: none

#module temps.py used to convert temperature units
#convert celsius to fahrenheit and display the results
#convert fahrenheit to celsius and return the results

#create void function with temp_celsius as a peremeter
def c_to_f(temp_celsius):
    #change celsius to fahrenheit and assign to variable temp_fahrenheit
    temp_fahrenheit = 9 / 5 * temp_celsius + 32
    #display results
    print(temp_celsius, 'Celsius equals', format(temp_fahrenheit, '.3f'), 'Fahrenheit')
#create function with temp_fahrenheit as a parameter
def f_to_c(temp_fahrenheit):
    #change fahrenheit to celsius and assign to variable temp_celsius
    temp_celsius = (temp_fahrenheit - 32) * (5 / 9)
    #return the value of temp_celsius
    return temp_celsius
