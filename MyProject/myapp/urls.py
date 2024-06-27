from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path('like/<int:card_id>/', like_card, name='like_card'),
    path("create/", create, name="create_card"),
    path("edit/<int:card_id>", edit, name="edit_card"),
    path("delete/<int:card_id>", delete_card, name="delete_card"),
]