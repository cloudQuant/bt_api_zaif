from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler
from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry


def register_zaif() -> None:
    from bt_api_zaif.feeds.live_zaif.spot import ZaifRequestDataSpot
    from bt_api_zaif.exchange_data import ZaifExchangeDataSpot

    ExchangeRegistry.register_feed("ZAIF___SPOT", ZaifRequestDataSpot)
    ExchangeRegistry.register_exchange_data("ZAIF___SPOT", ZaifExchangeDataSpot)
    ExchangeRegistry.register_balance_handler("ZAIF___SPOT", simple_balance_handler)


def plugin_info() -> PluginInfo:
    from bt_api_zaif import __version__

    return PluginInfo(
        name="Zaif",
        version=__version__,
        core_requires="bt_api_base",
        supported_exchanges=("ZAIF___SPOT",),
        supported_asset_types=("SPOT",),
        plugin_module="bt_api_zaif",
    )
