from __future__ import annotations

import hashlib
import hmac
import urllib.parse
from typing import Any

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_base.feeds.feed import Feed
from bt_api_base.feeds.http_client import HttpClient
from bt_api_zaif.exchange_data import ZaifExchangeDataSpot


class ZaifRequestData(Feed):
    _exchange_data = ZaifExchangeDataSpot()

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)
        self.exchange_name = kwargs.get("exchange_name", "ZAIF___SPOT")
        self.asset_type = kwargs.get("asset_type", "SPOT")
        self.api_key = kwargs.get("public_key") or kwargs.get("api_key") or ""
        self.api_secret = (
            kwargs.get("private_key") or kwargs.get("api_secret") or kwargs.get("secret_key") or ""
        )
        self.secret = self.api_secret
        self._params = self._exchange_data
        self._http_client = HttpClient(
            venue=self.exchange_name, timeout=kwargs.get("timeout", 10.0)
        )
        self._last_params: dict[str, Any] = {}

    def _get_signature(self, params: dict) -> str:
        encoded_params = urllib.parse.urlencode(sorted(params.items()))
        return hmac.new(
            self.secret.encode("utf-8"), encoded_params.encode("utf-8"), hashlib.sha512
        ).hexdigest()

    def _get_headers(self) -> dict[str, str]:
        return {
            "Key": self.api_key,
            "Sign": self._get_signature(self._last_params),
            "Content-Type": "application/x-www-form-urlencoded",
        }

    def _build_url(self, path: str, params: dict[str, Any] | None = None) -> str:
        base_url = self._exchange_data.get_rest_url().rstrip("/")
        request_path = path if path.startswith("/") else f"/{path}"
        if not params:
            return f"{base_url}{request_path}"
        return f"{base_url}{request_path}?{urllib.parse.urlencode(params)}"

    def request(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        body: Any = None,
        extra_data: Any = None,
        timeout: float = 10.0,
    ) -> RequestData:
        request_params = params or {}
        self._last_params = dict(request_params)
        response = self._http_client.request(
            method="GET",
            url=self._build_url(path, request_params),
            headers=self._get_headers(),
            json_data=body,
            timeout=timeout,
        )
        return RequestData(response, extra_data)

    async def async_request(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        body: Any = None,
        extra_data: Any = None,
        timeout: float = 10.0,
    ) -> RequestData:
        request_params = params or {}
        self._last_params = dict(request_params)
        response = await self._http_client.async_request(
            method="GET",
            url=self._build_url(path, request_params),
            headers=self._get_headers(),
            json_data=body,
            timeout=timeout,
        )
        return RequestData(response, extra_data)

    def async_callback(self, future: Any) -> None:
        if self.data_queue is None:
            return
        self.data_queue.put(future.result())

    def connect(self) -> None:
        return None

    def is_connected(self) -> bool:
        return True

    def _format_market(self, symbol: str) -> str:
        return symbol.lower()

    @staticmethod
    def _is_error(response: dict) -> bool:
        if not isinstance(response, dict):
            return False
        return response.get("error") is not None or response.get("success", 1) == 0

    def disconnect(self) -> None:
        super().disconnect()
