from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    # posts = Post.objects.filter(published = True)
    posts_page = Paginator(Post.objects.filter(published = True),2) # 2 es el nro de posts que quiero que entren en cada pagina
    page = request.GET.get('page') # me devuelve el nro actual de pagina en la que estoy
    posts = posts_page.get_page(page) # pido que me devuelva los posts que están en la pagina actual

    aux = "x" * posts.paginator.num_pages # me va a generar una variable con tantas x como nros de pagina haya,
                                            # esto me va a servir en el template para generar los nros de pagina en el paginador
    
    return render(request, 'core/home.html', {'posts': posts,
                                              'aux': aux})

def post(request, post_id):
    # post = Post.objects.get(id=post_id)
    try:
        post = get_object_or_404(Post, id=post_id)
        return render(request, "core/detail.html", {"post": post})
    except:
        return render(request, "core/404.html")

# FILTRADO POR CATEGORIA
def category(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        
        # posts = Post.objects.filter(category=category)
        
        return render(request, "core/category.html", {"category": category})
    except:
        return render (request, "core/404.html")

def author(request, author_id):
    try:
        author = get_object_or_404(User, id = author_id)
        return render(request, "core/author.html", {"author": author})
    except:
        return render(request, "core/404.html")

def dates(request):
    return render(request, "core/home.html")
