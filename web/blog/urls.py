from django.urls import path
from .views import index,blogdetail,searchCategory,about



urlpatterns = [
    path('',index,name="index"),
    path('blog/<slug:name_slug>',blogdetail,name="blogdetail"),
    path('blog/category/<int:cate_id>',searchCategory,name="category"),
    path('about/',about, name="about"),
]
