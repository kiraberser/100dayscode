MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def restOfResources(coffe):
    if coffe in MENU:
        for ingredient in MENU[coffe]["ingredients"]:
            if ingredient in resources:
                resources[ingredient] -= MENU[coffe]["ingredients"][ingredient] 

def validInput(money):
    while True:
        value = float(input(money))
        try:
            if value < 0:
                print(f"The value cannot be negative({value})")
                return False
            else: 
                return value
        except value as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

def enoughResources(coffe):
    if coffe in MENU:
        for ingredient in MENU[coffe]["ingredients"]:
            if ingredient in resources:
                if resources[ingredient] < MENU[coffe]["ingredients"][ingredient]:
                    print(f"Sorry there is not enough {ingredient}")
                    return False
        return True
    else:
        print(f"Sorry we don't have {coffe}")

def change(quarters, dimes, nickles, pennies, coffee):
    valueOfCoffee = MENU[coffee]["cost"]
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if total >= valueOfCoffee:
        change = total - valueOfCoffee
        print(f"Here is ${change:.2f} in change")
        print(f"There is your {coffee}🍵 Enjoy!")
        resources["money"] += valueOfCoffee
    else:
        print("Sorry that's not enough money. Money refunded")

def game():
    game_over = False
    resources["money"] = 0
    while not game_over:
        choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choose == "report":
            print(f" Water: {resources["water"]}ml\n Milk: {resources["milk"]}ml \n Coffee: {resources["coffee"]}g \n Money: ${resources['money']}")
        elif choose == "off":
            print("Good Bye!")
            game_over = True
        elif choose in ["espresso", "latte", "cappuccino"]:
            if enoughResources(choose):
                quarters = validInput("How many quarters?: ")
                dimes = validInput("How many dimes?: ")
                nickles = validInput("How many nickles?: ")
                pennies = validInput("How many pennies?: ")
                change(quarters, dimes, nickles, pennies, choose)
                restOfResources(choose)
        else:
            print("Invalid choice. Please choose again.")
game()
        

        
