import pytest
from vendingmachine.adapter import adapt_beverage, adapt_ingredients
from vendingmachine.models import Coffee, Ingredients

BEVERAGES_TEST_CASES = [
    ('BlackCoffee', False, Coffee(1, 3, 0, 1)),
    ('BlackCoffee', True, Coffee(1, 3, 0, 0)),
    ('MilkCoffee', False, Coffee(1, 1, 2, 1)),
    ('MilkCoffee', True, Coffee(1, 1, 2, 0))
]

INGREDIENTS_TEST_CASES = [
    ({'coffee': 1, 'milk': 2, 'sugar': 3, 'water': 0}, Ingredients(1, 2, 3, 0)),
    ({'coffee': 1}, Ingredients(1, 0, 0, 0)),
    ({'coffee': 1, 'Milk': 2, 'suGar': 3, 'water': 3}, Ingredients(1, 0, 0, 3)),
]


class TestAdaptBeverage(object):

    def test_invalid_beverages(self):
        with pytest.raises(NotImplementedError) as exception:
            adapt_beverage("MusicCoffee")
        assert str(exception.value) == 'Beverage `MusicCoffee` is not available'
        assert not adapt_beverage(beverage_str=None)
        assert not adapt_beverage(beverage_str=123)

    @pytest.mark.parametrize("beverage_str, sugarless, expected_beverage", BEVERAGES_TEST_CASES)
    def test_valid_beverages(self, beverage_str, sugarless, expected_beverage):
        beverage = adapt_beverage(beverage_str, sugarless)
        assert isinstance(beverage, Coffee)
        assert beverage.coffee == expected_beverage.coffee
        assert beverage.milk == expected_beverage.milk
        assert beverage.sugar == expected_beverage.sugar
        assert beverage.water == expected_beverage.water


class TestAdaptIngredients(object):

    def test_invalid_ingredients(self):
        assert not adapt_ingredients(None)
        assert not adapt_ingredients('Apple')

    @pytest.mark.parametrize("ingredient_dict, expected_ingredients", INGREDIENTS_TEST_CASES)
    def test_valid_ingredients(self, ingredient_dict, expected_ingredients):
        ingredients = adapt_ingredients(ingredient_dict)
        assert isinstance(ingredients, Ingredients)
        assert ingredients.coffee == expected_ingredients.coffee
        assert ingredients.milk == expected_ingredients.milk
        assert ingredients.sugar == expected_ingredients.sugar
        assert ingredients.water == expected_ingredients.water
