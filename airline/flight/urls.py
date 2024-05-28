from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("lalibella", views.lalibella, name="lalibella"),
    path("form", views.form, name="form"),
    path("insertuser", views.insertuser, name="insertuser"),
]
