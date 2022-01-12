from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display=('nome', 'email')
    display_link=('id', 'nome')
    search_fields=('nome',)

admin.site.register(Pessoa, ListandoPessoas)