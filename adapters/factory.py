from typing import Union

from adapters.credentials import CredentialsStore
from adapters.enums import AdapterType
from .telegram.adapter import TelegramAdapter
from .vk.adapter import VkAdapter


def create_adapter(adapter_type: AdapterType, credentials=None) -> Union[VkAdapter, TelegramAdapter, None]:
    adapters_map = {
        AdapterType.TELEGRAM: TelegramAdapter,
        AdapterType.VK: VkAdapter
    }

    adapter_class = adapters_map.get(adapter_type, TelegramAdapter)

    if credentials is None:
        credentials = CredentialsStore().get_credentials_for(adapter_type)
    adapter = adapter_class(credentials=credentials)

    return adapter
