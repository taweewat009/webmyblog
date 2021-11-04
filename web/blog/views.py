from django.shortcuts import render
from category.models import Category
from .models import Blogs 
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


def blogdetail(request, id):
    blogdetail = Blogs.objects.get(id=id)
    return render(request,'blogdetail.html',{'blogdetail':blogdetail})


def searchCategory(request,category_id):
    categories = Category.objects.all()
    search = Blogs.objects.filter(id=category_id)

    blog = Blogs.objects.all()

    last = Blogs.objects.all().order_by('-pk')[:1]

    return render(request, 'searchcategory.html',{'search':search,'categories':categories,'last':last,'blog':blog})
    