from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name='core/index.html'


class SobreView(TemplateView):
    template_name='core/sobre.html'