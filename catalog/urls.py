from django.urls import path

from catalog.views import (
    index,
    BookListView,
    LiteraryFormatListView,
    AuthorListView,
    BookDetailView,
    AuthorDetailView,
    test_session_view,
    LiteraryFormatCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("literary-formats/create/", LiteraryFormatCreateView.as_view(), name="literary-format-create"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("test-session/", test_session_view, name="test-session"),
]

app_name = "catalog"
