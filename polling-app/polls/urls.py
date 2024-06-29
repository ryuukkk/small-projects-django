from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.index_2, name="index_2")
]