from django.contrib import admin
from .models import Review

# Register your models here.

# @admin.register(Review)
# class PostAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',), }

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'status', 'published')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Review, ReviewAdmin)
