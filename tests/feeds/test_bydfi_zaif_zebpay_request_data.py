"""Module-level docstring."""
from unittest.mock import MagicMock
from bt_api_zaif.feeds.live_zaif.request_base import ZaifRequestData
from bt_api_zebpay.feeds.live_zebpay.request_base import ZebpayRequestData


def test_zaif_disconnect_closes_http_client() -> None:
    """test_zaif_disconnect_closes_http_client function"""
    request_data = ZaifRequestData()
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()


def test_zebpay_disconnect_closes_http_client() -> None:
    """test_zebpay_disconnect_closes_http_client function"""
    request_data = ZebpayRequestData()
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()


def test_zaif_falls_back_to_api_credentials_when_aliases_are_empty() -> None:
    """test_zaif_falls_back_to_api_credentials_when_aliases_are_empty function"""
    request_data = ZaifRequestData(
        public_key="",
        api_key="public-key",
        secret_key="",
        api_secret="secret-key",
    )

    assert request_data.api_key == "public-key"
    assert request_data.api_secret == "secret-key"


def test_zebpay_falls_back_to_api_credentials_when_aliases_are_empty() -> None:
    """test_zebpay_falls_back_to_api_credentials_when_aliases_are_empty function"""
    request_data = ZebpayRequestData(
        public_key="",
        api_key="public-key",
        secret_key="",
        api_secret="secret-key",
    )

    assert request_data.api_key == "public-key"
    assert request_data.api_secret == "secret-key"
