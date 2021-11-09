from django.urls import path
from .views import index,blogdetail,about



urlpatterns = [
    path('',index,name="index"),
    path('category/<slug:category_slug>',index,name="category"),
    path('blog/<slug:category_slug>/<slug:post_slug>',blogdetail,name="blogdetail"),
   
    #path('blog/<slug:slug>',blogdetail,name="blogdetail"),
    path('about/',about, name="about"),
]