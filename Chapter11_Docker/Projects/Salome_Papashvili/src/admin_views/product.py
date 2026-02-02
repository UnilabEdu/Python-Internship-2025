from src.admin_views.base import SecureModelView
from flask_admin.form import ImageUploadField
from src.config import Config
from os import path
from uuid import uuid4
from markupsafe import Markup

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class TourView(SecureModelView):
    create_modal = True
    edit_modal = True
    column_editable_list = ("price", "title")
    column_filters = ("price", "title", "country")
    column_formatters = {
        "title": lambda v, c, m, n: m.title if len(m.title) < 24 else m.title[:16] + "...",
        "description": lambda v, c, m, n: m.description if len(m.description) < 24 else m.description[:16] + "...",
        "image": lambda v, c, m, n: Markup(f"<img src='/static/upload/{m.image}' width='64' />")
    }
    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }