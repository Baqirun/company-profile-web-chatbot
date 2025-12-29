from django.urls import path
from .views import chat_hx,  main_page

urlpatterns = [
    path("chat/", chat_hx),
    path("",  main_page),
]
