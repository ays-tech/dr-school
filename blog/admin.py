from django.contrib import admin
from .models import Comment, Post




class CommentInline(admin.TabularInline): # new
    model = Comment

    
class PostAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)