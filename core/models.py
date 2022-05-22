from django.db import models
from stdimage.models import StdImageField
import uuid


# Image protection

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]  # pegar a extensao
    filename = f'{uuid.uuid4()}.{ext}'  # pegar caracteres dinamicos que ficam variando e colocando na imagem
    return filename  # e mais a protencao do django.


# Create your models here.

class Base(models.Model):
    criado = models.DateField('Criacao', auto_now_add=True)  # so eh colocado na add
    modificado = models.DateField('Atualizacao', auto_now=True)  # sempre que modifica, ele muda
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICE = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'User'),
        ('lni-layers', 'Designer'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviços', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICE)

    class Meta:  # para apresentar os dados com acentos e caracteres especial e vai aparecer
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo',
                              on_delete=models.CASCADE)  # remover em cascata, se tirar da outra lista e tambem ele
    # vai puxar as infos da outra tabela
    bio = models.TextField('Bio', max_length=100)
    image = StdImageField('Image', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    # lembrando que o django tem protecao contra a duplicidade de imagens, usando o STDImage ( usar ele sempre)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome
