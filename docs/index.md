# ZAIF API Reference

## English | [中文](#中文)

### Exchange Code

`ZAIF___SPOT`

### Exchange Info

| Item | Value |
|------|-------|
| REST URL | `https://api.zaif.jp` |
| WebSocket URL | `wss://ws.zaif.jp:8888` |
| Asset Type | SPOT |
| Plugin Entry | `bt_api_zaif.plugin:register_zaif` |

### Supported Capabilities

| Capability | Supported |
|------------|-----------|
| GET_TICK | ✅ |
| GET_DEPTH | ✅ |
| GET_KLINE | ✅ |
| GET_EXCHANGE_INFO | ✅ |
| GET_BALANCE | ✅ |
| GET_ACCOUNT | ✅ |
| MAKE_ORDER | ✅ |
| CANCEL_ORDER | ✅ |

### REST Endpoints

| Action | Path | Description |
|--------|------|-------------|
| ticker | `/api/1/ticker/{symbol}` | Price ticker for symbol |
| depth | `/api/1/depth/{symbol}` | Order book depth |
| trades | `/api/1/trades/{symbol}` | Recent trades |
| candles | `/api/1/candles/{symbol}` | OHLCV candle data |
| markets | `/api/1/markets` | Available markets |
| balance | `/api/1/account_balance` | Account balance |

### Kline Periods

| Period | Zaif Value |
|--------|-------------|
| 1m | 1 |
| 5m | 5 |
| 15m | 15 |
| 30m | 30 |
| 1h | 60 |
| 4h | 240 |
| 1d | 1440 |

### API Usage

```python
from bt_api import BtApi

# Initialize
api = BtApi(
    exchange_kwargs={
        "ZAIF___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker
ticker = api.get_tick("ZAIF___SPOT", "BTC_JPY")

# Get depth
depth = api.get_depth("ZAIF___SPOT", "BTC_JPY", count=20)

# Get klines
bars = api.get_kline("ZAIF___SPOT", "BTC_JPY", period="1h", count=100)

# Get balance
balance = api.get_balance("ZAIF___SPOT")

# Place order
order = api.make_order("ZAIF___SPOT", "BTC_JPY", volume=0.001, price=5000000, order_type="limit")

# Cancel order
api.cancel_order("ZAIF___SPOT", "BTC_JPY", order_id="your_order_id")
```

### Container — ZaifExchangeDataSpot

```python
from bt_api_zaif import ZaifExchangeDataSpot

info = ZaifExchangeDataSpot()
print(info.get_rest_url())          # https://api.zaif.jp
print(info.get_wss_url())           # wss://ws.zaif.jp:8888
print(info.get_kline_periods())     # { "1m": "1", "5m": "5", ... }
print(info.get_rest_path("ticker")) # /api/1/ticker/{symbol}
print(info.get_symbol("BTC_JPY"))  # btc_jpy
print(info.get_local_symbol("btc_jpy"))  # BTC_JPY
```

---

## 中文

### 交易所代码

`ZAIF___SPOT`

### 交易所信息

| 项目 | 值 |
|------|-----|
| REST URL | `https://api.zaif.jp` |
| WebSocket URL | `wss://ws.zaif.jp:8888` |
| 资产类型 | SPOT |
| 插件入口 | `bt_api_zaif.plugin:register_zaif` |

### 支持的能力

| 能力 | 支持状态 |
|------|---------|
| GET_TICK | ✅ |
| GET_DEPTH | ✅ |
| GET_KLINE | ✅ |
| GET_EXCHANGE_INFO | ✅ |
| GET_BALANCE | ✅ |
| GET_ACCOUNT | ✅ |
| MAKE_ORDER | ✅ |
| CANCEL_ORDER | ✅ |

### REST 端点

| 动作 | 路径 | 说明 |
|------|------|------|
| ticker | `/api/1/ticker/{symbol}` | 交易对价格行情 |
| depth | `/api/1/depth/{symbol}` | 订单簿深度 |
| trades | `/api/1/trades/{symbol}` | 最近成交 |
| candles | `/api/1/candles/{symbol}` | OHLCV K线数据 |
| markets | `/api/1/markets` | 可用市场列表 |
| balance | `/api/1/account_balance` | 账户余额 |

### K线周期

| 周期 | Zaif 值 |
|------|---------|
| 1m | 1 |
| 5m | 5 |
| 15m | 15 |
| 30m | 30 |
| 1h | 60 |
| 4h | 240 |
| 1d | 1440 |

### API 用法

```python
from bt_api import BtApi

# 初始化
api = BtApi(
    exchange_kwargs={
        "ZAIF___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# 获取行情
ticker = api.get_tick("ZAIF___SPOT", "BTC_JPY")

# 获取深度
depth = api.get_depth("ZAIF___SPOT", "BTC_JPY", count=20)

# 获取K线
bars = api.get_kline("ZAIF___SPOT", "BTC_JPY", period="1h", count=100)

# 获取余额
balance = api.get_balance("ZAIF___SPOT")

# 下单
order = api.make_order("ZAIF___SPOT", "BTC_JPY", volume=0.001, price=5000000, order_type="limit")

# 撤单
api.cancel_order("ZAIF___SPOT", "BTC_JPY", order_id="your_order_id")
```

### 容器类 — ZaifExchangeDataSpot

```python
from bt_api_zaif import ZaifExchangeDataSpot

info = ZaifExchangeDataSpot()
print(info.get_rest_url())          # https://api.zaif.jp
print(info.get_wss_url())          # wss://ws.zaif.jp:8888
print(info.get_kline_periods())     # { "1m": "1", "5m": "5", ... }
print(info.get_rest_path("ticker")) # /api/1/ticker/{symbol}
print(info.get_symbol("BTC_JPY"))  # btc_jpy
print(info.get_local_symbol("btc_jpy"))  # BTC_JPY
```
