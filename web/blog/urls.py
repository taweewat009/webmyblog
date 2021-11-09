from django.urls import path
from .views import index,blogdetail,searchCategory,about



urlpatterns = [
    path('',index,name="index"),
    path('<slug:slug>/<slug:post_slug>',blogdetail,name="blogdetail"),
    path('blog/category/<slug:slug>',searchCategory,name="category"),
    path('about/',about, name="about"),
]