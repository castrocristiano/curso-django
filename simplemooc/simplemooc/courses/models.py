from django.db import models

'''
    Herança: Todas as classes que representam entidades de banco devem herdar de models.Model.
    
    Para preparar as tabelas para geração, executar o comando: python manage.py makemigrations
    Para gerar, executar o comando: migrate --run-syncdb
'''


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now_add=True)
