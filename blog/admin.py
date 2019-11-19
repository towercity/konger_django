from django.contrib import admin
from .models import Post, Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',) 
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)

admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)