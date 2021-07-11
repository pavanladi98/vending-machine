from enum import Enum


class Coffee:
    def __init__(self, coffee, water, milk, sugar) -> None:
        self.coffee = coffee
        self.water = water
        self.milk = milk
        self.sugar = sugar


class Beverages(Coffee, Enum):
    """Beverages supported"""
    BlackCoffee = 1, 3, 0, 1
    MilkCoffee = 1, 1, 2, 1

    def sugarless(beverage: Coffee):
        beverage.sugar = 0
        return beverage
