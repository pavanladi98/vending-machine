from vendingmachine.models import Coffee, BlackCoffee, MilkCoffee, BlackCoffeeSugarless,\
    MilkCoffeeSugarless, Ingredients


def adapt_beverage(beverage_str: str, sugarless: bool = False) -> Coffee:
    if not beverage_str:
        return
    beverage_str = beverage_str.lower()
    if beverage_str == 'blackcoffee':
        return BlackCoffeeSugarless if sugarless else BlackCoffee
    if beverage_str == 'milkcoffee':
        return MilkCoffeeSugarless if sugarless else MilkCoffee
    raise NotImplementedError('Beverage `%s` is not available' % beverage_str)


def adapt_ingredients(request):
    ingredients = Ingredients()
    ingredients.milk = request.get('milk') or 0
    ingredients.water = request.get('water') or 0
    ingredients.sugar = request.get('sugar') or 0
    ingredients.coffee = request.get('coffee') or 0
    return ingredients
