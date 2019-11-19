from django.contrib import admin
from .models import Post, Page

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class PageAdmin(PostAdmin):
    list_display = ('title', 'slug', 'status', 'sidebar', 'created_on')
    list_filter = ("status", "sidebar",)

admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)