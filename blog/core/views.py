from django.shortcuts import render
from .models import Post
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

def post(request):
    return render(request, "core/detail.html")

def category(request):
    return render(request, "core/home.html")

def author(request):
    return render(request, "core/home.html")

def dates(request):
    return render(request, "core/home.html")
