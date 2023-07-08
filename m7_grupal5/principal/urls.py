from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("user_detail/<int:id_number>", views.user_detail, name="user_detail"),
    path("user_form", views.user_form, name="user_form"),
    path("user_register", views.user_form, name="user_register"),
    path('login', views.users_login, name='user_login'),
    path('logout', views.users_logout, name='user_logout'),
    path("about", views.about, name="about")
]