import logging
import re

from telethon import events, functions
from telethon.tl.types import InputPeerEmpty, InputPeerSelf

from app.handlers.handler import HandlerDecorator
from app.loader import client

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

bot_username = 'send'

link_pattern = fr"t\.me\/{bot_username}\?start=([A-Za-z0-9]+)"


async def handler(event):
    matches = re.findall(link_pattern, event.stringify())

    if not matches:
        return

    crypto_bot = await client.get_entity(f'@{bot_username}')

    for match in set(matches):
        print(match)
        # await client.send_message(
        #     '@CryptoBot',
        #     f'/start {match}'
        # )
        result = await client(functions.messages.StartBotRequest(
            bot=crypto_bot,
            peer=InputPeerSelf(),
            start_param=match
        ))
        print(result.stringify())


checks_decorator_new = HandlerDecorator(
    events.NewMessage(),
    handler
)

checks_decorator_edited = HandlerDecorator(
    events.MessageEdited(),
    handler
)