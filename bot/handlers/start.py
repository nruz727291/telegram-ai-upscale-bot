from pyrogram import filters
from pyrogram.types import Message

from bot.client import app


@app.on_message(filters.command("start"))
async def start_handler(_, message: Message):

    text = """
👋 **Welcome to AI Upscale Bot**

Send an image with:

`/upscale`

The bot will enhance and upscale your image using AI.

⚡ Fast Processing
🖼 High Quality Enhancement
🤖 Powered by Replicate AI

Developer: @Naruto_464
"""

    await message.reply_text(text)

print("START HIT")
