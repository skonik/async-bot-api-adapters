import os
from dataclasses import dataclass

from adapters.enums import AdapterType


@dataclass
class VkCredentials:
    token: str
    api_version: str

    adapter_type = AdapterType.VK

    @classmethod
    def from_env(cls):
        return cls(
            token=os.environ.get('VK_TOKEN'),
            api_version=os.environ.get('VK_API_VERSION')
        )
