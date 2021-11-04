from django.urls import path
from .views import index,blogdetail,searchCategory



urlpatterns = [
    path('',index,name="index"),
    path('blog/<int:id>',blogdetail,name="blogdetail"),
    path('blog/category/<int:category_id>',searchCategory,name="category"),
]