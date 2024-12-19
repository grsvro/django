from django.urls import path

from . import views

# 紐付け的なやつ

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
]
