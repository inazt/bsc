from django.contrib import admin
from bsc.planetarium.models import Blog, Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
