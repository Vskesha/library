from django.urls import path

from catalog.views import hello_world, index

urlpatterns = [
    path("hello/<int:unique_number>/", hello_world, name="hello"),
    path("", index, name="index"),
]

app_name = "catalog"
