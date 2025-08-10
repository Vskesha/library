from django.urls import path

from catalog.views import index, BookListView, LiteraryFormatListView, AuthorListView

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
]

app_name = "catalog"
