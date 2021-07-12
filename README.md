## How to run API

### setup virtual environment

- `python3 -m virtualenv .venv`
- `source .venv/bin/activate`

### install requirements

- `pip install -Ur requirements.txt`

### run application

- `python src/app.py`

### run test cases

- `pytest tests/`

## Assumptions:

1. Multiple ingredients can be toppedup at a time.
2. There should be a subscriber of `Topic.INSUFFICIENT_INGREDIENTS` to receive a notification when inventory runout of ingredients.


## API Signature:
1. `GET /api/beverages`

2. `GET /api/dispense?beverage=BlackCoffee&sugarless=true`

3. `POST /api/inventory/topup`
    ```
    {
        "coffee": 3,
        "sugar": 2,
        "milk": 2,
        "water": 3
    }
    ```
    