from .models import Ingredients, Coffee, Beverages
from .inventory import Inventory


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
        ingredients = Ingredients.get_ingredients_from_beverage(beverage)
        self._remove_ingredients(ingredients)

    def _verify_beverage(self, ingredients: Ingredients, beverage: Coffee) -> bool:
        if not any([beverage.coffee > ingredients.coffee, beverage.sugar > ingredients.sugar, beverage.milk > ingredients.milk,
                    beverage.water > ingredients.water]):
            return True
        return False

    def get_available_beverages(self) -> list:
        ingredients = self.inventory.display()
        available_beverages = []
        available_sugarless_beverages = []
        for beverage in Beverages:
            if self._verify_beverage(ingredients, beverage):
                available_beverages.append(beverage.name)
                available_sugarless_beverages.append(beverage.name)
                continue
            sugarless_beverage = Beverages.sugarless(beverage)
            if self._verify_beverage(ingredients, sugarless_beverage):
                available_sugarless_beverages.append(sugarless_beverage.name)
        return {'sugar': available_beverages, 'sugarless': available_sugarless_beverages}
