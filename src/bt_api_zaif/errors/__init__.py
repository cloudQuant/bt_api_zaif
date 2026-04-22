from __future__ import annotations

from typing import Any

from bt_api_base.error import ErrorTranslator


class ZaifErrorTranslator(ErrorTranslator):
    @staticmethod
    def is_error(response: dict[str, Any]) -> bool:
        if not isinstance(response, dict):
            return False
        return response.get('error') is not None or response.get('success', 1) == 0
