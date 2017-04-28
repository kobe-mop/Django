from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Blog
 
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','created')

class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagPostAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Blog,BlogPostAdmin)	
admin.site.register(Category,CategoryPostAdmin)
admin.site.register(Tag,TagPostAdmin)
