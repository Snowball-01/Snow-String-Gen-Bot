import asyncio
import logging
from pyromod import listen

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait

import config

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("oldpyro").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

mongo = MongoCli(config.MONGO_DB_URI)
db = mongo.StringGen


class Anony(Client):
    def __init__(self):
        super().__init__(
            name="Anonymous",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
        user_list = []
        async for user in db.users.find({"user_id": {"$gt": 0}}):
            user_list.append(user['user_id'])
        
        for id in user_list:
            try:
                await self.send_message(id, "<b>๏[-ิ_•ิ]๏ bot restarted !</b>")
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await self.send_message(id, "<b>๏[-ิ_•ิ]๏ bot restarted !</b>")
            except Exception:
                pass

    async def stop(self):
        await super().stop()


Anony = Anony()
