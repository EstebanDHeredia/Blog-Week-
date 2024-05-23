from .models import About, Link, Category

# ABOUT
def ctx_dic_about(request):
    
    ctx_about = {}

    ctx_about['ABOUT'] = About.objects.latest('created') # BUSCA EL ULTIMO CAMPO CREADO EN ABOUT (DE ACUERDO A LA FECHA DE CREACIÓN)

    return ctx_about

# CATEGORIAS
def ctx_dic_category(request):
    ctx_category = {}
    ctx_category['categories'] = Category.objects.filter(active=True)
    return ctx_category
    
# REDES SOCIALES
def ctx_dic_link(request):
    
    ctx_link = {}
    links = Link.objects.all()
    
    # GENERO UN DICCIONARIO CON TODOS LOS ELEMENTOS DE LA TABLA LINK
    for link in links:
        ctx_link[link.key] = {'url': link.url,
                                'icon': link.icon}
    print(ctx_link)

    return ctx_link

def ctx_dic_link2(request):
    
    ctx_link2 = {}
    ctx_link2['redes_sociales'] = Link.objects.all() 
    print(ctx_link2)

    return ctx_link2



# ARCHIVOS
