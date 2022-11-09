MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,

        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 150,
            "milk": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 300,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made,False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough{item}")
            is_enough = False
    return is_enough


def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please Insert A Coin.")
    total = int(input("How many quaters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_recived, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕")


is_on = True

while is_on:
    choice = input("what would you like?(esspersso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
