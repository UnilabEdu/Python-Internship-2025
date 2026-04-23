from MyPage.src.admin_views.base import SecureModelView
from markupsafe import Markup
from MyPage.src.admin_views.utils import generate_filename

from MyPage.src.config import Config
from flask_admin.form import ImageUploadField


class ProductView(SecureModelView):

    create_modal = True
    edit_modal = True

    details_modal = True

    column_labels = {
        'price': 'ფასი',
        'name': 'სახელი',
        'surname': 'გვარი',
        'img': 'სურათი'
    }


    column_searchable_list = ("name","img")
    column_filters = ("price",)
    column_formatters = {
        "img": lambda v,c,m,n: Markup(f"<img src = '/static/uploads/{m.img}' width = 128>")
    }

    column_list = ("img", "name",'surname','price')
    form_overrides = {"img": ImageUploadField}
    form_args = {"img": {
        "base_path": Config.UPLOAD_PATH,
        "namegen": generate_filename

    }}



