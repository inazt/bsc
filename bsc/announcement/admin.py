from django.contrib import admin
from bsc.announcement.models import News, Event

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
