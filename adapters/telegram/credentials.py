import os
from dataclasses import dataclass

from adapters.enums import AdapterType


@dataclass
class TelegramCredentials:
    token: str

    adapter_type = AdapterType.TELEGRAM

    @classmethod
    def from_env(cls):
        print(os.environ.get('TELEGRAM_TOKEN'))
        return cls(
            token=os.environ.get('TELEGRAM_TOKEN')
        )
