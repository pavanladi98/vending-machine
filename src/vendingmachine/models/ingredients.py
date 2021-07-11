

class Ingredients:
    def __init__(self, coffee: int = 0, milk: int = 0, sugar: int = 0, water: int = 0) -> None:
        self.coffee = coffee
        self.milk = milk
        self.sugar = sugar
        self.water = water

    def isempty(self):
        return not any([self.coffee, self.milk, self.sugar, self.water])
