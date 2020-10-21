import io

from adapters.base import BaseAdapter
from aiogram import Bot

from adapters.enums import AdapterType


class TelegramAdapter(BaseAdapter):
    adapter_type = AdapterType.TELEGRAM

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bot = Bot(token=self.credentials.token)

    async def send_image(self, chat_id: int, image: io.FileIO) -> None:
        await self.bot.send_photo(chat_id=chat_id, photo=image)

    async def send_message(self, chat_id: int, text: str, **kwargs) -> None:
        await self.bot.send_message(chat_id=chat_id, text=text)
