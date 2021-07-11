from flask import Flask, request, abort, jsonify, make_response
from vendingmachine import Inventory, CoffeeVendingMachine
from vendingmachine.exceptions import InsufficientIngredientsException, IngredientsOverflowException
from vendingmachine.adapter import adapt_beverage, adapt_ingredients
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
INVENTORY = Inventory(water_capacity=30, sugar_capacity=20, milk_capacity=30, coffee_capacity=30)


@app.route('/isalive', methods=['GET'])
def isalive():
    """isalive url"""
    return ("VendingMachine API - I'm Alive"
            "<br/>Maintainer: <a href='mailto:pavanladi98@gmail.com'>Pavan Kalyan Ladi</a><br/>")


@app.route('/api/beverages', methods=['GET'])
def display_beverages():
    """Display available beverages at the moment"""
    try:
        vendingmachine = CoffeeVendingMachine(inventory=INVENTORY)
        available_beverages = vendingmachine.get_available_beverages()
        return jsonify({'beverages': available_beverages})
    except Exception as err:
        error_response = jsonify({'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


@app.route('/api/dispense', methods=['GET'])
def dispense_beverage():
    """dispense requested beverage"""
    request_args = request.args
    try:
        beverage = adapt_beverage(request_args.get('beverage'), request_args.get('sugarless'))
        if not beverage:
            response = jsonify({'status': 'INVALID_REQUEST',
                                'message': 'Provide a beverage - blackcoffee, milkcoffee'})
            return abort(make_response(response, 400))
        vendingmachine = CoffeeVendingMachine(inventory=INVENTORY)
        vendingmachine.dispense_beverage(beverage)
        return jsonify({'status': 'SUCCESS', 'message': 'Beverage dispensed'})
    except HTTPException:
        raise
    except NotImplementedError as err:
        error_response = jsonify({'status': 'NOT_SUPPORTED', 'message': err.args})
        return abort(make_response(error_response, 422))
    except InsufficientIngredientsException:
        return jsonify({'status': 'NOT_AVAILABLE',
                        'message': 'Insufficient ingredients to dispense %s' % request_args.get('beverage')})
    except Exception as err:
        error_response = jsonify({'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


@app.route('/api/inventory/topup', methods=['POST'])
def topup_inventory():
    """Add ingredients to the inventory"""
    request_json = request.json
    try:
        ingredients = adapt_ingredients(request_json)
        if ingredients.isempty():
            response = jsonify({'status': 'INVALID_REQUEST',
                               'message': 'Provide atleast one of the ingredients - coffee, sugar, milk, water'})
            return abort(make_response(response, 400))
        vendingmachine = CoffeeVendingMachine(inventory=INVENTORY)
        vendingmachine.add_ingredients(ingredients)
        return jsonify({'status': 'SUCCESS'})
    except HTTPException:
        raise
    except TypeError as err:
        response = jsonify({'status': 'INVALID_REQUEST', 'message': err.args})
        return abort(make_response(response, 400))
    except IngredientsOverflowException as err:
        error_response = jsonify({'status': 'FAILED', 'message': err.args})
        return abort(make_response(error_response, 400))
    except Exception as err:
        error_response = jsonify({'status': 'UNKNOWN_ERROR', 'message': err.args})
        return abort(make_response(error_response, 500))


if __name__ == '__main__':
    app.run('0.0.0.0', 3000)
