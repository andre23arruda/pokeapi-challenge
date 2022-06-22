from django.contrib import admin
from django.conf.locale.pt_BR import formats as portuguese
from django.conf.locale.en import formats as english
from .models import Pokemon

portuguese.DATE_FORMAT = 'd/m/Y'
english.DATE_FORMAT = 'd/m/Y'

@admin.register(Pokemon)
class PokemonRegister(admin.ModelAdmin):
    list_display = ['number', 'name', 'types', 'created_at']
    list_display_links = ['number', 'name']
    list_per_page = 25
    list_filter = ['types']
    search_fields = ['number', 'name']
    ordering = ['number']
