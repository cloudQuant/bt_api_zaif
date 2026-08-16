"""Module-level docstring."""
from __future__ import annotations

from bt_api_zaif.exchange_data import ZaifExchangeData, ZaifExchangeDataSpot
from bt_api_zaif.feeds.live_zaif.request_base import ZaifRequestData
from bt_api_zaif.feeds.live_zaif.spot import ZaifRequestDataSpot
from bt_api_zaif.plugin import plugin_info, register_zaif

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "ZaifExchangeData",
    "ZaifExchangeDataSpot",
    "ZaifRequestData",
    "ZaifRequestDataSpot",
    "plugin_info",
    "register_zaif",
]
