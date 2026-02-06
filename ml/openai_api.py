import os

import openai
from dotenv import load_dotenv

from config.directories import images_dir

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY", "")
size = os.environ.get("OPENAI_IMAGE_SIZE", "1024x1024")


def get_variants():
    """
    Get variants of the generated image from the OpenAI API using DALL-E.
    :return: OpenAI API response containing image variation data.
    """
    image_path = images_dir / "canvas.png"

    openai.api_key = api_key

    with open(image_path, mode="rb") as image_file:
        response = openai.Image.create_variation(
            image=image_file,
            n=1,
            size=size,
            response_format="b64_json",
        )

    return response
