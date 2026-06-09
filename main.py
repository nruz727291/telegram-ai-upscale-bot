import uvloop
import asyncio
import logging

uvloop.install()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

from bot.client import app

import bot.handlers.start
import bot.handlers.upscale


async def main():

    await app.start()

    me = await app.get_me()

    print(f"✅ Bot Started -> @{me.username}")

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
