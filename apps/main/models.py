from math import trunc

from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField('Фио', max_length=50)
    email = models.EmailField('Электронная почта', max_length=70)
    subject = models.CharField('Тема', max_length=50)
    text = models.TextField('Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Subscription(models.Model):
    email = models.EmailField('Электронная почта', max_length=70)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'