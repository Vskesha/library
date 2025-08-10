from django.urls import path

from catalog.views import index, LiteraryFormatListView

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
]

app_name = "catalog"
