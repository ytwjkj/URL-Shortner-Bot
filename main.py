import os
from pyrogram import Client

bot_token = os.environ["6136957569:AAEm1vJ9Dq98-hsKglCFdkE-FgclPJFafAc"]
api_id = int(os.environ["27171791"])
api_hash = os.environ["ab263db210a44b8e2657387246f2cd90"]
plugins = dict(
    root="plugins"
)

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
