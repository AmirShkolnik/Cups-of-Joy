from django.contrib import admin
from .models import Mom, Dad
# Register your models here.

class MomAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')

admin.site.register(Mom, MomAdmin)

class DadAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')

admin.site.register(Dad, DadAdmin)