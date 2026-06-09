import os
import aiohttp

from pyrogram import filters
from pyrogram.types import Message

from bot.client import app
from bot.services.replicate_api import upscale_image
from bot.utils.helpers import generate_filename


@app.on_message(filters.command("upscale"))
async def upscale_handler(_, message: Message):

    replied = message.reply_to_message

    if not replied or not replied.photo:
        return await message.reply_text(
            "❌ Reply to an image with /upscale"
        )

    processing = await message.reply_text(
        "⏳ Upscaling image..."
    )

    input_path = generate_filename()

    try:

        await replied.download(
            file_name=input_path
        )

        output_url = await upscale_image(
            input_path
        )

        output_path = generate_filename()

        async with aiohttp.ClientSession() as session:
            async with session.get(output_url) as resp:

                if resp.status != 200:
                    raise Exception(
                        "Failed to download upscaled image"
                    )

                with open(output_path, "wb") as f:
                    f.write(await resp.read())

        await message.reply_photo(
            photo=output_path,
            caption="✅ Image upscaled successfully"
        )

        await processing.delete()

        os.remove(input_path)
        os.remove(output_path)

    except Exception as e:

        await processing.edit_text(
            f"❌ Error:\n`{str(e)}`"
        )

        if os.path.exists(input_path):
            os.remove(input_path)
