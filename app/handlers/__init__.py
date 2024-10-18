from telethon import TelegramClient, events

from app.handlers.checks import checks_decorator_new, checks_decorator_edited

active_decorators = [
    checks_decorator_new,
    checks_decorator_edited
]


def register_active_handlers(client: TelegramClient):
    for decorator in active_decorators:

        client.add_event_handler(
            decorator.handler,
            decorator.event
        )

