from django.contrib import admin
from account.models import CustomUser

@admin.register(CustomUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('created',)
    search_fields = ('username', )


