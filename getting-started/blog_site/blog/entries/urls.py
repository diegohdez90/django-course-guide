from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'), 
    path("posts", views.posts, name='posts'), 
    path("posts/<slug:slug>", views.post, name='post'), 
    # path("posts/<int:id>"),
]
