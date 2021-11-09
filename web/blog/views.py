from django.shortcuts import render
from category.models import Category
from .models import Blogs, PhotoAlbum 
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.

    
def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()

    last = Blogs.objects.all().order_by('-pk')[:1]
    

    #paginator การแบ่งเพจ
    paginator = Paginator(blogs, 9)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        blogperpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        blogperpage = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html',{'categories':categories,'blogs':blogperpage,'last':last})


def blogdetail(request, slug):
    blogdetail = Blogs.objects.get(slug=slug)
    blogdetail.views = blogdetail.views + 1
    blogdetail.save()
    return render(request,'blogdetail.html',{'blogdetail':blogdetail})


def searchCategory(request,slug):
    categories = Category.objects.all()
    search = Blogs.objects.filter(slug=slug)
    
    

    blogs = Blogs.objects.all()

    last = Blogs.objects.all().order_by('-pk')[:1]
    template_name = 'searchcategory.html'

    return render(request,'searchcategory.html',{'search':search,'categories':categories,'last':last,'blogs':blogs,'template_name':template_name})


def about(request):
    photos = PhotoAlbum.objects.all()
    return render(request, 'about.html',{'photos':photos})