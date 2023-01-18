
import os
from config.directories import images_dir

import openai

from config.api import api_key, size

from config.directories import images_dir


def get_variants():
    image_path = images_dir / "canvas.png"

    openai.api_key = api_key

    response = openai.Image.create_variation(
        image=open(image_path, mode="rb"),
        n=1,
        size=size,
        response_format="b64_json",
    )

    return response
