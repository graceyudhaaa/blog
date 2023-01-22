import base64
from io import BytesIO
import os
import secrets
from PIL import Image
from flask import current_app
import numpy as np


def flatten_2d_list(xss):
    return [x for xs in xss for x in xs]


def save_image(form_picture, output_size=None):
    random_hex = secrets.token_hex(8)
    # blank one suppose to be filename
    _, file_extension = os.path.splitext(form_picture.filename)
    pic_filename = random_hex + file_extension
    pic_path = f"{current_app.root_path}/static/user_upload/images/{pic_filename}"

    image = Image.open(form_picture)

    if output_size:
        image.thumbnail(output_size, Image.ANTIALIAS)
    image.save(pic_path, optimize=True, quality=20, dpi=[300, 300])

    return pic_filename

def save_image_b64(form_picture, output_size=None):
    random_hex = secrets.token_hex(8)
    # blank one suppose to be filename
    _, file_extension = os.path.splitext(form_picture.filename)
    pic_filename = random_hex + file_extension

    image = Image.open(form_picture)

    if output_size:
        image.thumbnail(output_size, Image.ANTIALIAS)
        
    buffer = BytesIO()

    if file_extension.lower() == '.jpg':
        format = 'jpeg'
    else:
        format = file_extension.lower()[1:]

    image.save(buffer,format=format)
    value = buffer.getvalue()                     
    # image.save(pic_path, optimize=True, quality=20, dpi=[300, 300])

    return f"data:image/{format};base64,{base64.b64encode(value).decode('utf-8')}"