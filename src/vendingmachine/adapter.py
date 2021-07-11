from vendingmachine.models import Coffee, Beverages, Ingredients


def adapt_beverage(beverage_str: str, sugarless: bool = False) -> Coffee:
    if not beverage_str or not isinstance(beverage_str, str):
        return
    for beverage in Beverages:
        if beverage.name == beverage_str:
            return Beverages.sugarless(beverage) if sugarless else beverage
    raise NotImplementedError('Beverage `%s` is not available' % beverage_str)


def adapt_ingredients(request: dict) -> Ingredients:
    if not request or not isinstance(request, dict):
        return
    return Ingredients.from_dict(request)
