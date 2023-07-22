""" 'Off' and 'report' are the secret codes of the machine 'off'
turns the machine off and 'report' checks the inventory of the machine"""

resource = {
    "water": 500,
    "sugar": 500,
    "milk": 500,
    "coffee": 500,
    "money": 0
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "sugar": 100,
            "milk": 0,
            "coffee": 100
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "sugar": 100,
            "milk": 100,
            "coffee": 100
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 100,
            "sugar": 100,
            "milk": 200,
            "coffee": 100
        },
        "cost": 4.5
    }
}

while True:
    total_amount = 0.0
    change = 0.0
    choose = input("Welcome!! What would you like?\n1 for espresso\n2 for latte\n3 for cappuccino\n4 for menu\nChoose:")
    if choose == "off":
        exit()
    elif choose == "report":
        for item in resource:
            print(f"{item.capitalize()}: {resource[item]}")
    elif choose in ["1", "2", "3"]:
        drink_name = ""
        drink_cost = 0.0

        if choose == "1":
            drink_name = "espresso"
            drink_cost = MENU[drink_name]["cost"]
        elif choose == "2":
            drink_name = "latte"
            drink_cost = MENU[drink_name]["cost"]
        elif choose == "3":
            drink_name = "cappuccino"
            drink_cost = MENU[drink_name]["cost"]

        if resource["water"] < MENU[drink_name]["ingredients"]["water"]:
            print("There is not enough water")
        elif resource["sugar"] < MENU[drink_name]["ingredients"]["sugar"]:
            print("There is not enough sugar")
        elif resource["milk"] < MENU[drink_name]["ingredients"]["milk"]:
            print("There is not enough milk")
        elif resource["coffee"] < MENU[drink_name]["ingredients"]["coffee"]:
            print("There is not enough coffee")
        else:
            print(f"Preparing {drink_name}. Cost: {drink_cost}")
            try:
                quarter, dime, nickel, pennies = map(float, input("How many quarters will you insert?\nHow many dimes will you insert?\nHow many nickels will you insert?\nHow many pennies will you insert?\n").split())
            except ValueError:
                print("Invalid input. Please enter the number of each coin.")
                continue
            total_amount = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.5) + (pennies * 0.01)
            print("Total amount inserted: $", total_amount)

            if total_amount == drink_cost:
                print(f"Here is your {drink_name}. Enjoy!")
                for item in MENU[drink_name]["ingredients"]:
                    resource[item] -= MENU[drink_name]["ingredients"][item]
                resource["money"] += drink_cost
            elif total_amount > drink_cost:
                change = total_amount - drink_cost
                print(f"Here is your change: ${change:.2f}")
                print(f"Here is your {drink_name}. Enjoy!")
                for item in MENU[drink_name]["ingredients"]:
                    resource[item] -= MENU[drink_name]["ingredients"][item]
                resource["money"] += drink_cost
            else:
                print("Not enough money. Money refunded")
