from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(max_length=200, verbose_name = 'Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = 'posts',
        verbose_name = 'Автор'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name = 'posts',
        blank=True,
        null=True,
        verbose_name = 'Группа')

            
class Meta:
    verbose_name_plural = 'Посты'
    ordering = ('-pub_date',)


def __str__(self):
    return self.text[0:30]
