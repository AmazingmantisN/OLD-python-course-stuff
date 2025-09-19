import Data
import art
import random


game_continue = True
current_resources = Data.resources
demand = ""
bank = 0


def moneyask():
    global quarters
    global dimes
    global nickels
    global pennies
    global total_paid
    global bank
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_paid = round(quarters * Data.MONEY['quarters'] + dimes * Data.MONEY['dimes'] + nickels * Data.MONEY ['nickels'] + pennies * Data.MONEY['pennies'] ,2)

    if total_paid >= Data.MENU[demand]['cost']:
        print(f"Here is your change ${total_paid - Data.MENU[demand]['cost']}.")
        print(f"Here is your {demand}. Enjoy your Drink!☕")
        bank += Data.MENU[demand]['cost']
        execution()

    elif total_paid < Data.MENU[demand]['cost']:
        print("Sorry that is not enough money. Money refunded")
        execution()

def check_resources():
    if demand == "cappuccino" or demand == "latte" or demand == "espresso":

        for x in Data.MENU[demand]['ingredients']:
            if Data.MENU[demand]['ingredients'][x] > current_resources[x]:
                print(f"Sorry, we dont have enough {x}")
                execution()
            else:
                for b in Data.MENU[demand]['ingredients']:
                    current_resources[b] = current_resources[b] - Data.MENU[demand]['ingredients'][b]
                moneyask()









def execution():
    global demand

    demand = input("  What would you like? (espresso/latte/cappuccino):  ")

    if demand == "report":
        print(f"Water : {current_resources['water']}\nMilk : {current_resources['milk']}\nCoffee : {current_resources['coffee']} \nMoney : ${bank}")
        execution()
    elif demand == "espresso" or demand == "latte" or demand == "cappuccino":
        check_resources()



while game_continue == True:
    execution()
