import replicate
import asyncio
from bot.config import REPLICATE_API_TOKEN

client = replicate.Client(api_token=REPLICATE_API_TOKEN)


async def upscale_image(image_path: str):

    loop = asyncio.get_event_loop()

    def run_prediction():
        with open(image_path, "rb") as image:
            output = client.run(
                "nightmareai/real-esrgan",
                input={
                    "image": image,
                    "scale": 4
                }
            )
            return output

    result = await loop.run_in_executor(
        None,
        run_prediction
    )

    return result
