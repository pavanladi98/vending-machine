from vendingmachine.models import coffee
from .models import Ingredients, Coffee, BlackCoffee, MilkCoffee, \
    BlackCoffeeSugarless, MilkCoffeeSugarless
from .inventory import Inventory
from enum import Enum


supported_beverages = [BlackCoffee, MilkCoffee, BlackCoffeeSugarless, MilkCoffeeSugarless]


class Beverages(Enum):
    """Beverages supported"""
    BlackCoffee = 'blackcoffee'
    MilkCoffee = 'milkcoffee'
    BlackCoffeeSugarless = 'blackcoffeesugarless'
    MilkCoffeeSugarless = 'milkcoffeesugarless'


class CoffeeVendingMachine:
    def __init__(self, inventory: Inventory) -> None:
        self.inventory = inventory
        self._validate()
        pass

    def _validate(self) -> None:
        if not isinstance(self.inventory, Inventory):
            raise TypeError('Expected instance of `class::Inventory`, got %s' % type(self.inventory))

    def add_ingredients(self, ingredients: Ingredients) -> None:
        self.inventory.add(ingredients)

    def _remove_ingredients(self, ingredients: Ingredients) -> None:
        self.inventory.remove(ingredients)

    def dispense_beverage(self, beverage: Coffee) -> None:
        ingredients = Ingredients(coffee=beverage.coffee, milk=beverage.milk,
                                  sugar=beverage.sugar, water=beverage.water)
        self._remove_ingredients(ingredients)

    def _verify_beverage(self, ingredients: Ingredients, beverage: Coffee) -> bool:
        if not any([beverage.coffee > ingredients.coffee, beverage.sugar > ingredients.sugar, beverage.milk > ingredients.milk,
                    beverage.water > ingredients.water]):
            return True
        return False

    def get_available_beverages(self) -> list:
        ingredients = self.inventory.display()
        available_beverages = []
        for beverage in supported_beverages:
            if self._verify_beverage(ingredients, beverage):
                available_beverages.append(beverage.__name__)
        return available_beverages
