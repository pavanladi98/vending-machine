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
1. Server will never restarts. So, inventory is persistent
2. Can topup multiple values at a time


## ToDos:
1. Add test cases
2. Add design diagram (High level, Low level?)
3. Add proper README.md
