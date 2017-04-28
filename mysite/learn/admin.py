from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Blog
 
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','created')


admin.site.register(Blog,BlogPostAdmin)	
admin.site.register([Category,Tag])


