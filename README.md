# Project Overview

This repository provides basic arithmetic utilities and accompanying tests.

## Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is absent, install `pytest` manually.)*

## Usage

The `src/calc.py` module exposes simple arithmetic functions:

```python
from src.calc import add, div

result = add(1, 2)
quotient = div(6, 3)
```

## Examples

Running the test suite demonstrates usage:

```bash
.venv/bin/pytest -q
```

