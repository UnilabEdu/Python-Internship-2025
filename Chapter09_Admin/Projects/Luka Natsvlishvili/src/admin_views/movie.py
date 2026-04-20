from flask import url_for
from src.admin_views.base import SecureModelView
from markupsafe import Markup
from flask_admin.form import ImageUploadField
from src.config import Config
from wtforms import SelectField

class MovieView(SecureModelView):
    create_modal = True
    edit_modal = True
    column_editable_list = ("comment1_author","comment1_text","comment2_author","comment2_text")
    can_view_details = True
    details_modal = True
    can_export = True
    column_labels = {
        "name" : "სახელი",
        "release_date": "გამოშვების წელი",
        "genre": "ჟანრი",
        "comment1_author": "პირველი კომენტარის ავტორი",
        "comment1_text": "პირველი კომენტარი",
        "comment2_author": "მეორე კომენტარის ავტორი",
        "comment2_text": "მეორე კომენტარი",
        "img": "სურათი"
    }
    column_searchable_list = ("name",)
    column_filters = ("release_date",)
    column_formatters = {
        "img": lambda v, c, m, n: Markup(
            f'<img src="{url_for("static", filename=str(m.img))}" width="100">'
        ) if m.img else "სურათი არაა"
    }
    column_list = ("img", "name", "comment1_author", "comment1_text","comment2_author", "comment2_text",)
    form_overrides = {"img": ImageUploadField, "genre": SelectField}
    form_args = {"img": {"base_path": Config.UPLOAD_PATH, "relative_path": "img/"},
                 "genre": {
                     "choices": ["კომედია", "საშინელებათა", "დრამა", "თრილერი","მძაფრსიუჟეტიანი","რომანტიკული","საშობაო","საოჯახო","სათავგადასავლო","ანიმაციური","დეტექტივი","ბიოგრაფიული","დოკუმენტური","ფანტასტიკა","ვესტერნი","ფენტეზი","მუსიკალური"]
                 }}


