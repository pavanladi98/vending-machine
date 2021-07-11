class Coffee:
    sugar = 0
    coffee = 0
    water = 0
    milk = 0


class BlackCoffee(Coffee):
    sugar = 1
    coffee = 1
    water = 3


class MilkCoffee(Coffee):
    sugar = 1
    coffee = 1
    water = 1
    milk = 2


class BlackCoffeeSugarless(BlackCoffee):
    sugar = 0


class MilkCoffeeSugarless(MilkCoffee):
    sugar = 0
