#まずはモデルをインポートする
#自分で作成したモデルのインポートは,で続けてok
from django import forms
from django.forms import ModelForm

from .models import Post, Comment, User

#投稿フォームの追加
class PostForm(forms.ModelForm):
    class Meta:
        model = Post      
        fields = ('author','text',)

#コメントフォームの追加
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('post','author', 'text',)

