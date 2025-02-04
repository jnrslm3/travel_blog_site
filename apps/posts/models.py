from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField('Название Категория', max_length=50, unique=True)
    slug = models.SlugField('Slug', max_length=70)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Теги', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField('Название поста', max_length=100)
    text = models.TextField('Text')
    image = models.ImageField('Фото поста', upload_to='posts')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
    tags = models.ManyToManyField(Tag, related_name='tag_post')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'