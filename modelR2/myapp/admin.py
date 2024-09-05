from django.contrib import admin

from . models import Post

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = [ 'user' , 'post_title' , 'post_publish_date' , 'post_cat']
