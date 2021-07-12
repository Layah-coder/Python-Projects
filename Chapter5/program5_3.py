#Leah Oswald
#2420610

#Collaboration: none

#Program for a shooter game.
#Import modules.
#Create a shoot function that generates a random number.
#Create a main function that calculates ammo and health.
#Display results.

#import random to generate random numbers
import random

#define shoot function
def shoot():
    #display 'shot fired'
    print('Shot fired. ', end = '')
    #generate random number 0 or 1
    your_shot = random.randint(0, 1) 
    #determine if your random number should return true or false
    if your_shot == 1:
        return True
    else:
        return False
#define main function
def main():
    #assign values to ammo and health
    ammo = 10
    health = 5
    #create while loop that executes as long as you have ammo
    while ammo > 0:
        result = shoot()
        #determine what to do if random number is true
        if result == True:
            print('Enemy was hit!')
            #subtract from health and ammo if true
            ammo -= 1
            health -= 1
            #determine if the health is less than 0
            if (health < 1):
                print('Enemy destroyed. you won!')
                print('GAME OVER')
                #use keyword break to stop loop
                break
        #determine what to do if result is not true
        else:
            print('Shot missed.')
            #subtract from ammo
            ammo -= 1
        #determine what to do if ammo runs out    
        if ammo == 0:
            print('You are out of ammo! You lose!')
            print('GAME OVER')
main()
