from adapters.enums import AdapterType
from adapters.telegram.credentials import TelegramCredentials
from adapters.vk.credentials import VkCredentials


class CredentialsStore(object):
    INCLUDED_CREDENTIALS = [TelegramCredentials, VkCredentials]

    def __init__(self, credentials_list: list = None) -> None:
        if credentials_list is None:
            credentials_list = []
            self.credentials_list = credentials_list
            self.load_from_env()
            print(self.credentials_list)

    def load_from_env(self) -> None:
        for credential_class in self.INCLUDED_CREDENTIALS:
            self.credentials_list.append(credential_class.from_env())

    def get_credentials_for(self, adapter_type: AdapterType):
        for credential in self.credentials_list:
            if credential.adapter_type == adapter_type:
                return credential

        return None
