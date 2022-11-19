from django.contrib import admin

from .models import Album, Musica

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_lancamento', 'publicado')
    search_fields = ['nome']

admin.site.register(Album, AlbumAdmin)


class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'album', 'audio', 'letra')
    search_fields = ['nome']

admin.site.register(Musica, MusicaAdmin)