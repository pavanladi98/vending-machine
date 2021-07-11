from .coffee import Coffee


class Ingredients:
    def __init__(self, coffee: int = 0, milk: int = 0, sugar: int = 0, water: int = 0) -> None:
        self.coffee = coffee
        self.milk = milk
        self.sugar = sugar
        self.water = water

    def isempty(self) -> bool:
        return not any([self.coffee, self.milk, self.sugar, self.water])

    @staticmethod
    def get_ingredients_from_beverage(beverage: Coffee):
        return Ingredients(beverage.coffee, beverage.milk, beverage.sugar, beverage.water)

    @staticmethod
    def from_dict(ingredients_dict: dict):
        """Returns Ingredients object from dictionary"""
        ingredients = Ingredients()
        if not ingredients_dict:
            return ingredients
        ingredients.water = ingredients_dict.get('water') or 0
        ingredients.milk = ingredients_dict.get('milk') or 0
        ingredients.coffee = ingredients_dict.get('coffee') or 0
        ingredients.sugar = ingredients_dict.get('sugar') or 0
        return ingredients
