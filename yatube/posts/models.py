from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    slug = models.SlugField(verbose_name='Имя', unique=True, max_length=50,)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст', max_length=200)
    pub_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа')

    class Meta:
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)


def __str__(self):
    return self.text[0:30]
