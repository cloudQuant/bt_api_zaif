from bt_api_base.feeds.capability import Capability
from bt_api_zaif.feeds.live_zaif.request_base import ZaifRequestData


class ZaifRequestDataSpot(ZaifRequestData):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_DEPTH,
            Capability.GET_KLINE,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
        }

    def __init__(self, data_queue=None, **kwargs):
        super().__init__(data_queue, **kwargs)
        self.exchange_name = kwargs.get("exchange_name", "ZAIF___SPOT")
