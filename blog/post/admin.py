from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'public', 'created', 'updated')
    list_filter = ('public', 'created')
    list_editable = ('public', )
    search_fields = ('title', 'content')


