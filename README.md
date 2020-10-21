### ‍⚕ WIP: Async Bot API Adapters ‍⚕
This package allows to interact with vk and telegram API using 
the same interface. 

It's main purpose is to simply switch 🕹 between services while developing bots.


## Setup
Firstly you should export environment variables.
Create `.env` file and fill vars:

```
TELEGRAM_TOKEN=telegram_token
VK_TOKEN=vk_token
```

## Example

Upload Images to vk and tg.

```python
import asyncio

import aiofiles

from adapters.factory import create_adapter
from adapters.enums import AdapterType
from dotenv import load_dotenv
load_dotenv()

tg_adapter = create_adapter(adapter_type=AdapterType.TELEGRAM)
vk_adapter = create_adapter(adapter_type=AdapterType.VK)


async def main():
    async with aiofiles.open('test.png', mode='rb') as data:
        content = await data.read()
        await asyncio.gather(*[
                tg_adapter.send_image(chat_id=-195789610, image=content),
                vk_adapter.send_image(chat_id=2000000006, image=content)
        ])

asyncio.run(main())


```