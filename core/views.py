from django.views.generic import TemplateView
from album.models import Album

class IndexView(TemplateView):
    template_name='core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albuns'] = Album.objects.filter(publicado=True)
        return context


class SobreView(TemplateView):
    template_name='core/sobre.html'