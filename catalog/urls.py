from django.urls import path

from catalog.views import index, BookListView, LiteraryFormatListView, AuthorListView, BookDetailView, \
    test_session_view, AuthorDetailView

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("test-session/", test_session_view, name="test-session"),
]

app_name = "catalog"
