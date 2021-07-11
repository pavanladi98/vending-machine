from .models.ingredients import Ingredients
from .exceptions import InsufficientIngredientsException, IngredientsOverflowException
from eventbus import Topic
from pubsub import pub


class Inventory:
    def __init__(self, water_capacity: int = 0, coffee_capacity: int = 0, milk_capacity: int = 0,
                 sugar_capacity: int = 0) -> None:
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
        max_water = self._water_capacity - self._water
        max_sugar = self._sugar_capacity - self._sugar
        max_milk = self._milk_capacity - self._milk
        if any([ingredients.coffee > max_coffee, ingredients.water > max_water, ingredients.sugar > max_sugar,
                ingredients.milk > max_milk]):
            raise IngredientsOverflowException('Max capacity available is coffee:{0}, milk:{1}, sugar:{2}, water:{3}'.format(
                max_coffee, max_milk, max_sugar, max_water))

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
            pub.sendMessage(Topic.INSUFFICIENT_INGREDIENTS, ingredients=self.display())
            raise InsufficientIngredientsException
        self._coffee -= ingredients.coffee
        self._milk -= ingredients.milk
        self._sugar -= ingredients.sugar
        self._water -= ingredients.water

    def display(self) -> Ingredients:
        return Ingredients(coffee=self._coffee, milk=self._milk, sugar=self._sugar, water=self._water)
