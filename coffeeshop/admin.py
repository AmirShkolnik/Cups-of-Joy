from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review

# Register your models here.

# @admin.register(Review)
# class PostAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',), }

class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'excerpt', 'status', 'published')
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Review, ReviewAdmin)