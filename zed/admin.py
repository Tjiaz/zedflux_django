from django.contrib import admin
from .models import BlogPost,BlogDetail

# Register your models here.




# admin.site.register(BlogPost,BlogDetail)


from django.contrib import admin
from .models import BlogPost, BlogDetail

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at']

@admin.register(BlogDetail)
class BlogDetailAdmin(admin.ModelAdmin):
    list_display = ['blog_post', 'content', 'comment', 'created_at']