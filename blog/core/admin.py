from django.contrib import admin
from .models import Category, Post, Tag, About, Link


admin.site.site_header = "Administración del Blog"
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Blog'

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'category', 'author', 'created', 'post_tags')
    ordering = ('author', '-created')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    list_filter = ('author', 'category', 'tags') # AGREGA UNA BARRA LATERAL CON FILTROS AUTOMATICOS

    def post_tags(self, obj):
        return ' - '.join([t.name for t in obj.tags.all().order_by('name')])
    
    post_tags.short_description = "Etiquetas"

# ABOUT
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description','created')
 
# REDES SOCIALES
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','key', 'url', 'icon')
    
admin.site.register(Link, LinkAdmin)
admin.site.register(About, AboutAdmin)    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
