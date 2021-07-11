from enum import Enum


class Coffee:
    def __init__(self, sugar, coffee, water, milk) -> None:
        self.sugar = sugar
        self.coffee = coffee
        self.water = water
        self.milk = milk


class Beverages(Coffee, Enum):
    """Beverages supported"""
    BlackCoffee = 1, 1, 3, 0
    MilkCoffee = 1, 1, 1, 2

    def sugarless(beverage: Coffee):
        beverage.sugar = 0
        return beverage
