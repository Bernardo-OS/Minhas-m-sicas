from django.views.generic import DetailView
from .models import Album

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album/album_detail.html'
