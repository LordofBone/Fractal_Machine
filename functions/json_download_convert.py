import json
from base64 import b64decode

from config.directories import *


def convert_b64_to_image(file_name, openai_response):
    json_file = data_dir / file_name

    with open(json_file, mode="r", encoding="utf-8") as file:
        response = json.load(file)

    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = images_dir / f"{json_file.stem}-{index}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)

    return image_file
