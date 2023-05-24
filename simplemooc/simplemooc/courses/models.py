from django.db import models
from django.urls import reverse


class CourseManager(models.Manager):
    """
        Herança: Todas as classes que representam entidades de banco devem herdar de models.Model.

        Para preparar as tabelas para geração, executar o comando: python manage.py makemigrations
        Para gerar, executar o comando: migrate --run-syncdb
    """

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    """ See: https://docs.djangoproject.com/pt-br/3.0/ref/models """
    id = models.AutoField('Código', primary_key=True)
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
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
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now_add=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Não funciona bem: return reverse('courses:details', (), {'slug': self.slug})
        return reverse('courses:details', args=[self.slug])

    class Meta:
        """
            Classe para definições de metadados dos modelos
        """
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
        """ 
            Usando ifen na frente ele ordena de forma decrescente
            Exemplo: ordering = ['-name']
        """
