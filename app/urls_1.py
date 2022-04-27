from django.urls import path
from.import views

urlpatterns = [
    path("",views.home , name = "home"),
    path("create_book",views.create_book , name = "create_book"),
    path("delete_book/<int:id>",views.delete_book , name = "delete_book"),
    path("update_book/<int:id>",views.update_book , name = "update_book")
]