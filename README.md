# bt_api_zaif

Zaif exchange adapter for bt_api.

## Installation

```bash
pip install bt_api_zaif
```

## Usage

```python
from bt_api_zaif import register_zaif
register_zaif()

from bt_api_py import BtApi
api = BtApi(exchange_kwargs={"ZAIF___SPOT": {"api_key": "...", "secret": "..."}})
ticker = api.get_tick("ZAIF___SPOT", "btc_jpy")
```
