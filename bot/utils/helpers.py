import os
import uuid

TEMP_DIR = "temp"

os.makedirs(TEMP_DIR, exist_ok=True)


def generate_filename(ext="jpg"):
    return os.path.join(
        TEMP_DIR,
        f"{uuid.uuid4()}.{ext}"
    )
