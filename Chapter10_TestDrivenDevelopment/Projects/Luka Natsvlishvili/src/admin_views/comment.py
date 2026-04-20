from src.admin_views.base import SecureModelView

class CommentView(SecureModelView):
    column_list = ("id", "author", "text", "movie_id")
    column_labels = {
        "id": "ID",
        "author": "ავტორი",
        "text": "კომენტარი",
        "movie_id": "ფილმი"
    }
    can_delete = True
    can_create = False
    can_edit = False