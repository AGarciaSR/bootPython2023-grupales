from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("user_detail/<int:id_number>", views.user_detail, name="user_detail"),
    path("new_provider", views.proveedor_create, name="new_provider"),
    path("about", views.about, name="about")
]