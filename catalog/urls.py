from django.urls import path

from catalog.views import index, literary_format_list_view

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", literary_format_list_view, name="literary-format-list"),
]

app_name = "catalog"
