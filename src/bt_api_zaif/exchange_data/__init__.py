from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class ZaifExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = 'ZAIF'


class ZaifExchangeDataSpot(ZaifExchangeData):
    _REST_URL = 'https://api.zaif.jp'
    _WSS_URL = 'wss://ws.zaif.jp:8888'
    _KLINE_PERIODS = {
        '1m': '1',
        '5m': '5',
        '15m': '15',
        '30m': '30',
        '1h': '60',
        '4h': '240',
        '1d': '1440',
    }
    _REST_PATHS = {
        'ticker': '/api/1/ticker/{symbol}',
        'depth': '/api/1/depth/{symbol}',
        'trades': '/api/1/trades/{symbol}',
        'candles': '/api/1/candles/{symbol}',
        'markets': '/api/1/markets',
        'balance': '/api/1/account_balance',
    }

    def __init__(self) -> None:
        super().__init__()
        self.rest_url = self._REST_URL
        self.wss_url = self._WSS_URL
        self.kline_periods = dict(self._KLINE_PERIODS)
        self.rest_paths = dict(self._REST_PATHS)

    def get_rest_url(self) -> str:
        return self.rest_url

    def get_wss_url(self) -> str:
        return self.wss_url

    def get_kline_periods(self) -> dict[str, str]:
        return dict(self.kline_periods)

    def get_symbol(self, symbol: str) -> str:
        return symbol.lower()

    def get_rest_path(self, action: str) -> str:
        return self.rest_paths.get(action, '')

    def get_wss_path(self, action: str) -> str:
        return ''

    def get_local_symbol(self, symbol: str) -> str:
        return symbol.upper()

    def is_trading_enabled(self) -> bool:
        return True
