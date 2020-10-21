from abc import abstractmethod


class BaseAdapter(object):

    def __init__(self, credentials):
        self.credentials = credentials

    @abstractmethod
    async def send_image(self, chat_id, image, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def send_message(self, chat_id, text, **kwargs):
        raise NotImplementedError
