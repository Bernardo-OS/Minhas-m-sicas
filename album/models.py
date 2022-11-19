from django.db import models


class Album(models.Model):
    nome = models.CharField('Nome do álbum', max_length=50)
    data_lancamento = models.DateField('Data do lançamento')
    publicado = models.BooleanField('Publicado', default=True)
    foto = models.ImageField('Foto da capa', upload_to='album/fotos')
    cor_fundo = models.TextField('Cor de fundo', default='#000000')
    cor_texto = models.CharField('Cor do texto', max_length=100, default='#FFFFFF')

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome = models.CharField('Nome da música', max_length=50)
    album = models.ForeignKey(Album, verbose_name='Álbum', on_delete=models.RESTRICT)
    audio = models.FileField('Áudio', upload_to='album/audios')
    letra = models.TextField('Letra')