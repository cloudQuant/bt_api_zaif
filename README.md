# ZAIF

Exchange plugin for bt_api framework — Japanese cryptocurrency exchange.

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_zaif.svg)](https://pypi.org/project/bt_api_zaif/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_zaif.svg)](https://pypi.org/project/bt_api_zaif/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_zaif/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_zaif/actions)
[![Docs](https://readthedocs.org/projects/bt-api-zaif/badge/?version=latest)](https://bt-api-zaif.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

[Zaif](https://zaif.jp/) is a **Japanese cryptocurrency exchange** licensed by the Japan Financial Services Agency (FSA), offering JPY trading pairs for Bitcoin and other cryptocurrencies. This plugin integrates Zaif into the [bt_api](https://github.com/cloudQuant/bt_api_py) unified trading framework, supporting **SPOT** markets.

### Features

- **REST API** — market data queries, order management, account queries
- **JPY trading pairs** — supports JPY (Japanese Yen) trading pairs
- **Japanese market focus** — licensed exchange compliant with Japanese regulations
- **Simple API key auth** — standard API key + secret authentication

### Exchange Code

| Code | Description | Asset Type |
|------|-------------|------------|
| `ZAIF___SPOT` | Zaif spot markets | SPOT |

### Installation

```bash
pip install bt_api_zaif
```

Or install from source:

```bash
git clone https://github.com/cloudQuant/bt_api_zaif
cd bt_api_zaif
pip install -e .
```

### Quick Start

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "ZAIF___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker data
ticker = api.get_tick("ZAIF___SPOT", "BTC_JPY")
print(ticker)

# Get order book
depth = api.get_depth("ZAIF___SPOT", "BTC_JPY", count=20)
print(depth)

# Get klines
bars = api.get_kline("ZAIF___SPOT", "BTC_JPY", period="1h", count=100)
print(bars)
```

### Supported Operations

| Operation | Status | Description |
|-----------|--------|-------------|
| Ticker | ✅ | Real-time price and 24h statistics |
| OrderBook/Depth | ✅ | Market depth and order book |
| Klines/Bars | ✅ | Historical OHLCV data |
| Exchange Info | ✅ | Trading rules and symbol info |
| Balance | ✅ | Account balance queries |
| Account | ✅ | Account information |
| Make Order | ✅ | Place limit/market orders |
| Cancel Order | ✅ | Cancel existing orders |

### API Reference

#### Feed — ZaifRequestDataSpot

Inherits from `ZaifRequestData`. Access via `BtApi`.

```python
api.get_tick("ZAIF___SPOT", "BTC_JPY")        # Ticker
api.get_depth("ZAIF___SPOT", "BTC_JPY")       # Order book
api.get_kline("ZAIF___SPOT", "BTC_JPY")       # Klines
api.get_exchange_info("ZAIF___SPOT")           # Exchange info
```

#### Container — ZaifExchangeDataSpot

Exchange metadata and configuration.

```python
from bt_api_zaif import ZaifExchangeDataSpot

info = ZaifExchangeDataSpot()
print(info.get_rest_url())    # https://api.zaif.jp
print(info.get_wss_url())     # wss://ws.zaif.jp:8888
print(info.get_kline_periods())  # { "1m": "1", "5m": "5", ... }
```

#### REST Endpoints

| Action | Path | Method |
|--------|------|--------|
| ticker | `/api/1/ticker/{symbol}` | GET |
| depth | `/api/1/depth/{symbol}` | GET |
| trades | `/api/1/trades/{symbol}` | GET |
| candles | `/api/1/candles/{symbol}` | GET |
| markets | `/api/1/markets` | GET |
| balance | `/api/1/account_balance` | GET |

### Architecture

```
bt_api_zaif/
├── src/bt_api_zaif/
│   ├── containers/      # ZaifExchangeDataSpot
│   ├── feeds/           # ZaifRequestDataSpot
│   ├── exchange_data/    # Exchange metadata
│   ├── errors/          # Error translation
│   └── plugin.py        # register_zaif()
└── docs/
    └── index.md         # Bilingual API docs
```

### Requirements

- Python 3.9+
- bt_api_base >= 0.15

### Online Documentation

| Resource | Link |
|----------|------|
| Full Docs | https://bt-api-zaif.readthedocs.io/ |
| Chinese Docs | https://bt-api-zaif.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_zaif |
| Issue Tracker | https://github.com/cloudQuant/bt_api_zaif/issues |

### License

MIT License — see [LICENSE](LICENSE) for details.

---

## 中文

### 概述

[Zaif](https://zaif.jp/) 是一家受 **日本金融厅 (FSA)** 许可的 **日本加密货币交易所**，提供比特币和其他加密货币的日元（JPY）交易对。本插件将 Zaif 接入 [bt_api](https://github.com/cloudQuant/bt_api_py) 统一交易框架，支持 **现货 (SPOT)** 市场。

### 功能特点

- **REST API** — 行情查询、订单管理、账户查询
- **日元交易对** — 支持 JPY（日本円）交易对
- **日本市场监管** — 合规持牌交易所
- **简单 API Key 认证** — 标准 API Key + Secret 认证方式

### 交易所代码

| 代码 | 描述 | 资产类型 |
|------|--------|----------|
| `ZAIF___SPOT` | Zaif 现货市场 | SPOT |

### 安装

```bash
pip install bt_api_zaif
```

或从源码安装：

```bash
git clone https://github.com/cloudQuant/bt_api_zaif
cd bt_api_zaif
pip install -e .
```

### 快速开始

```python
from bt_api import BtApi

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
print(ticker)

# 获取订单簿
depth = api.get_depth("ZAIF___SPOT", "BTC_JPY", count=20)
print(depth)

# 获取K线
bars = api.get_kline("ZAIF___SPOT", "BTC_JPY", period="1h", count=100)
print(bars)
```

### 支持的操作

| 操作 | 状态 | 说明 |
|------|------|------|
| 行情 (Ticker) | ✅ | 实时价格和24小时统计 |
| 订单簿 (OrderBook) | ✅ | 市场深度和挂单 |
| K线 (Klines) | ✅ | 历史OHLCV数据 |
| 交易所信息 | ✅ | 交易规则和交易对信息 |
| 余额 (Balance) | ✅ | 账户余额查询 |
| 账户 (Account) | ✅ | 账户信息 |
| 下单 (Make Order) | ✅ | 限价/市价下单 |
| 撤单 (Cancel Order) | ✅ | 取消现有订单 |

### API 参考

#### Feed — ZaifRequestDataSpot

继承自 `ZaifRequestData`，通过 `BtApi` 访问。

```python
api.get_tick("ZAIF___SPOT", "BTC_JPY")        # 行情
api.get_depth("ZAIF___SPOT", "BTC_JPY")       # 订单簿
api.get_kline("ZAIF___SPOT", "BTC_JPY")       # K线
api.get_exchange_info("ZAIF___SPOT")           # 交易所信息
```

#### Container — ZaifExchangeDataSpot

交易所元数据和配置。

```python
from bt_api_zaif import ZaifExchangeDataSpot

info = ZaifExchangeDataSpot()
print(info.get_rest_url())    # https://api.zaif.jp
print(info.get_wss_url())     # wss://ws.zaif.jp:8888
print(info.get_kline_periods())  # { "1m": "1", "5m": "5", ... }
```

#### REST 端点

| 动作 | 路径 | 方法 |
|------|------|------|
| ticker | `/api/1/ticker/{symbol}` | GET |
| depth | `/api/1/depth/{symbol}` | GET |
| trades | `/api/1/trades/{symbol}` | GET |
| candles | `/api/1/candles/{symbol}` | GET |
| markets | `/api/1/markets` | GET |
| balance | `/api/1/account_balance` | GET |

### 项目结构

```
bt_api_zaif/
├── src/bt_api_zaif/
│   ├── containers/      # ZaifExchangeDataSpot
│   ├── feeds/           # ZaifRequestDataSpot
│   ├── exchange_data/    # 交易所元数据
│   ├── errors/          # 错误翻译
│   └── plugin.py        # register_zaif()
└── docs/
    └── index.md         # 中英文API文档
```

### 系统要求

- Python 3.9+
- bt_api_base >= 0.15

### 在线文档

| 资源 | 链接 |
|------|------|
| 完整文档 | https://bt-api-zaif.readthedocs.io/ |
| 中文文档 | https://bt-api-zaif.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_zaif |
| 问题反馈 | https://github.com/cloudQuant/bt_api_zaif/issues |

### 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。
