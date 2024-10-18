from typing import Callable

from telethon.events.common import EventBuilder


class HandlerDecorator:
    def __init__(
            self,
            event: EventBuilder,
            handler: Callable
    ):
        self.event = event
        self.handler = handler
