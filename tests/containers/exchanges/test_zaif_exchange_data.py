"""Tests for ZaifExchangeData container."""

from __future__ import annotations

from bt_api_zaif.exchange_data import ZaifExchangeData


class TestZaifExchangeData:
    """Tests for ZaifExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = ZaifExchangeData()

        assert exchange.exchange_name == "ZAIF"
