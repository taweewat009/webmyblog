from django.shortcuts import render,get_object_or_404
from category.models import Category
from .models import Blogs, PhotoAlbum 
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.

    
def index(request,category_slug=None):
    blogs = None
    category_page = None
    if category_slug != None:
        category_page=get_object_or_404(Category,slug=category_slug)
        blogs = Blogs.objects.all().filter(category=category_page)
    else:
        blogs = Blogs.objects.all()
    
      
    return render(request, 'index.html',{'blogs':blogs,'category':category_page})


def blogdetail(request,category_slug,post_slug):
    try:
        blogdetail = Blogs.objects.get(category__slug=category_slug,slug=post_slug)
        blogdetail.views = blogdetail.views + 1
        blogdetail.save()
    except Exception as e :
        raise e
    return render(request,'blogdetail.html',{'blogdetail':blogdetail})
    
    
    ''' 
    blogdetail = Blogs.objects.get(slug=slug)
    blogdetail.views = blogdetail.views + 1
    blogdetail.save()
    return render(request,'blogdetail.html',{'blogdetail':blogdetail})
    '''

'''  
#def searchCategory(request,category_slug):
    categories = Category.objects.all()
    search = Blogs.objects.filter(slug=category_slug)
    blogs = Blogs.objects.all()
    last = Blogs.objects.all().order_by('-pk')[:1]
    template_name = 'searchcategory.html'

    return render(request,'searchcategory.html',{'search':search,'categories':categories,'last':last,'blogs':blogs,'template_name':template_name})
 '''

def about(request):
    photos = PhotoAlbum.objects.all()
    return render(request, 'about.html',{'photos':photos})