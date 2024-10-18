from app.handlers import register_active_handlers
from app.loader import client


register_active_handlers(client)

client.start()
client.run_until_disconnected()
