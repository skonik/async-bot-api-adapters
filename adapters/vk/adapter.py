import asyncio
import json

import aiohttp
from aiovk import TokenSession, API
from aiovk.drivers import HttpDriver

from adapters.base import BaseAdapter
from adapters.enums import AdapterType


class VkAdapter(BaseAdapter):
    adapter_type = AdapterType.VK

    @property
    def vk(self):
        if not hasattr(self, 'vk_api'):
            loop = asyncio.get_event_loop()
            connector = aiohttp.TCPConnector(verify_ssl=False)
            session = aiohttp.ClientSession(connector=connector)
            driver = HttpDriver(loop=loop, session=session)
            self.session = TokenSession(access_token=self.credentials.token, driver=driver)
            self.vk_api = API(self.session)

        return self.vk_api


    async def send_image(self, chat_id, image, **kwargs):
        response = await self.vk.photos.getMessagesUploadServer(peer_id=chat_id)
        upload_url = response['upload_url']
        form_data = aiohttp.FormData()
        form_data.add_field('photo', image, filename='photo.jpg')

        async with self.session.driver.session.post(upload_url, data=form_data) as resp:
            upload = await resp.read()
            response = json.loads(upload)

        url_img = await self.vk.photos.saveMessagesPhoto(
            photo=response['photo'], server=response['server'],
            hash=response['hash']
        )

        attachment = f"photo{url_img[0]['owner_id']}_{url_img[0]['id']}"

        await self.send_message(chat_id=chat_id, attachment=attachment, **kwargs)

    async def send_message(self, chat_id, text=' ', **kwargs):
        await self.vk_api.messages.send(peer_id=chat_id, message=text, **kwargs)