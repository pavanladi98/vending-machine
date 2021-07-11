from .models.ingredients import Ingredients
from .exceptions import InsufficientIngredientsException, IngredientsOverflowException


class Inventory:
    def __init__(self, water_capacity=0, coffee_capacity=0, milk_capacity=0, sugar_capacity=0) -> None:
        self._coffee = 0
        self._milk = 0
        self._sugar = 0
        self._water = 0
        self._water_capacity = water_capacity
        self._coffee_capacity = coffee_capacity
        self._milk_capacity = milk_capacity
        self._sugar_capacity = sugar_capacity

    def add(self, ingredients: Ingredients) -> None:
        if not isinstance(ingredients, Ingredients):
            raise TypeError('Expected instance of `class::Ingredients`, got %s' % type(ingredients))
        if ingredients.isempty():
            raise ValueError('No ingredients provided to add into inventory')
        max_coffee = self._coffee_capacity - self._coffee
        if ingredients.coffee > max_coffee:
            raise IngredientsOverflowException('Max coffee can be added is %s' % max_coffee)
        max_water = self._water_capacity - self._water
        if ingredients.water > max_water:
            raise IngredientsOverflowException('Max water can be added is %s' % max_water)
        max_sugar = self._sugar_capacity - self._sugar
        if ingredients.sugar > max_sugar:
            raise IngredientsOverflowException('Max sugar can be added is %s' % max_sugar)
        max_milk = self._milk_capacity - self._milk
        if ingredients.milk > max_milk:
            raise IngredientsOverflowException('Max milk can be added is %s' % max_milk)

        self._coffee += ingredients.coffee
        self._milk += ingredients.milk
        self._sugar += ingredients.sugar
        self._water += ingredients.water

    def remove(self, ingredients: Ingredients) -> None:
        if not isinstance(ingredients, Ingredients):
            raise TypeError('Expected instance of `class::Ingredients`, got %s' % type(ingredients))
        if ingredients.isempty():
            raise ValueError('No ingredients provided to remove from inventory')
        if any([ingredients.coffee > self._coffee, ingredients.sugar > self._sugar, ingredients.milk > self._milk,
                ingredients.water > self._water]):
            raise InsufficientIngredientsException
        self._coffee -= ingredients.coffee
        self._milk -= ingredients.milk
        self._sugar -= ingredients.sugar
        self._water -= ingredients.water

    def display(self) -> Ingredients:
        return Ingredients(coffee=self._coffee, milk=self._milk, sugar=self._sugar, water=self._water)
