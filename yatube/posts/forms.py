from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError('Заполните текст поста!')
        return text