import asyncio
import logging
from aiohttp import web

from bot.client import app
import bot.handlers.start
import bot.handlers.upscale

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

async def health_check(request):
    return web.Response(text="Bot Running")

async def start_webserver():
    web_app = web.Application()
    web_app.router.add_get("/", health_check)

    runner = web.AppRunner(web_app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

async def main():
    await app.start()

    me = await app.get_me()
    print(f"✅ Bot Started -> @{me.username}")

    await start_webserver()

    # 🔥 CRITICAL FIX: keep Pyrogram alive properly
    await app.idle()


if __name__ == "__main__":
    asyncio.run(main())
