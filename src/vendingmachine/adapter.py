from vendingmachine.models import Coffee, Beverages, Ingredients


def adapt_beverage(beverage_str: str, sugarless: bool = False) -> Coffee:
    if not beverage_str or not isinstance(beverage_str, str):
        return
    for beverage in Beverages:
        if beverage.name == beverage_str:
            x = Beverages.sugarless(beverage) if sugarless else beverage
            return x
    raise NotImplementedError('Beverage `%s` is not available' % beverage_str)


def adapt_ingredients(request):
    ingredients = Ingredients()
    ingredients.milk = request.get('milk') or 0
    ingredients.water = request.get('water') or 0
    ingredients.sugar = request.get('sugar') or 0
    ingredients.coffee = request.get('coffee') or 0
    return ingredients
