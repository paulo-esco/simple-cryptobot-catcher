import configparser

from telethon import TelegramClient

config = configparser.ConfigParser()
config.read('app/config/client.ini')


class AppCredentials:
    def __init__(self, config_section):
        self.session_name = config_section["session_name"]
        self.app_id = int(config_section["app_id"])
        self.app_hash = config_section["app_hash"]
        self.device_model = config_section["device_model"]
        self.system_version = config_section["system_version"]
        self.app_version = config_section["app_version"]


# Создание экземпляра с параметрами из конфигурации
app_credentials = AppCredentials(config["app_credentials"])

client = TelegramClient(
    app_credentials.session_name,
    app_credentials.app_id,
    app_credentials.app_hash,
    device_model=app_credentials.device_model,
    system_version=app_credentials.system_version,
    app_version=app_credentials.app_version
)
