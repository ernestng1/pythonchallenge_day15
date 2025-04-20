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
    "money": 0
}

def coffee_machine(menu, resources):
    machine_setting = input("What would you like? (espresso/latte/cappuccino) ")
    if machine_setting == "off":
        return print("The coffee machine has been switched off.")
    elif machine_setting == "report":
        print(f"Water: {resources["water"]}ml\n"
              f"Milk: {resources["milk"]}ml\n"
              f"Coffee: {resources["coffee"]}ml\n"
              f"Money: ${resources["money"]}")
        coffee_machine(menu, resources)
    elif machine_setting in ["espresso", "latte", "cappuccino"]:
        if check_machine(menu, machine_setting)[0] == False:
            print(f"Sorry, there is not enough {check_machine(menu, machine_setting)[1]}")
            coffee_machine(menu, resources)
        elif check_machine(menu, machine_setting)[0] == True:
            print("Please insert coin\n")
            quarter_input = input("How many quarters?: ")
            dimes_input = input("How many dimes?: ")
            nickles_input = input("How many nickles?: ")
            pennies_input = input("How many pennies?: ")
            total_amount = int(quarter_input)*0.25+int(dimes_input)*0.10+int(nickles_input)*0.05+int(pennies_input)*0.01
            if total_amount >= menu[machine_setting]["cost"]:
                print(f"Here is ${round(total_amount - menu[machine_setting]["cost"],2)} dollars in change")
                resources["money"] += menu[machine_setting]["cost"]
                for i in menu[machine_setting]["ingredients"]:
                    resources[i] -= menu[machine_setting]["ingredients"][i]
                print(f"Enjoy your {machine_setting}")
                coffee_machine(menu, resources)
            else:
                print("Sorry that's not enough money. Money refunded.")
                coffee_machine(menu, resources)

def check_machine(menu, drink):
    sufficient = True
    insufficient_resources = []
    for i in menu[drink]["ingredients"]:
        if resources[i] <= menu[drink]["ingredients"][i]:
            sufficient = False
            insufficient_resources.append(i)
    return  sufficient, insufficient_resources

coffee_machine(MENU, resources)