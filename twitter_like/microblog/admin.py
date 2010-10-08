from django.contrib import admin
from twitter_like.microblog.models import MicroBlog, Tweet

class MicroBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    prepopulated_fields = {'slug': ('name',)}


class TweetAdmin(admin.ModelAdmin):
    list_display = ('message', 'author', 'created')


admin.site.register(MicroBlog, MicroBlogAdmin)
admin.site.register(Tweet, TweetAdmin)
