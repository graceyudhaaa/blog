import os
import secrets
from flask import (
    Blueprint,
    current_app,
    request,
    url_for,
    send_from_directory
)

from flask_ckeditor import upload_fail, upload_success

ckeditor_controller = Blueprint("ckeditor_controller", __name__, template_folder="templates", static_folder="static")

# @ckeditor_controller.route('/files/<filename>')
# def uploaded_files(filename):
#     path = current_app.config['UPLOADED_PATH']
#     return send_from_directory(path, filename)


@ckeditor_controller.route('/upload', methods=['POST'])
def upload():
    random_hex = secrets.token_hex(4)
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    filename = f.filename.split('.')
    filename[0] += f"_{random_hex}"
    print(filename)
    filename = ".".join(filename)
    f.save(os.path.join(current_app.config['UPLOADED_PATH'], filename))
    url = url_for('static', filename=f"user_upload/images/{filename}")
    return upload_success(url, filename=filename)