from src.admin_views.base import SecureModelView
from wtforms.fields import SelectField
from os import path
from uuid import uuid4
from flask_admin.form import ImageUploadField
from src.config import Config

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class UserView(SecureModelView):
    can_create = True
    can_edit = False
    can_delete = False
    can_view_details = True
    create_modal = True
    edit_modal = True
    # column_exclude_list = ["_password"]
    column_list = ["username", "role"]
    column_details_list = ["username", "role", "profile_image"]
    column_searchable_list = ["username", "role"]

    form_overrides = {
        "profile_image": ImageUploadField,
        "role": SelectField
    }

    form_args = {
        "profile_image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        },
        "role": {
            "choices": ["Admin", "Moderator", "User"]
        }
    }
