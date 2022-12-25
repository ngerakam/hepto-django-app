from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ChoiceField, EmailInput, FileField, ModelForm, TextInput, Textarea

from .models import Article, Tag, Category
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ArticlesForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'author', 'category', 'content', 'picture', 'tag']

    def __init__(self, *args, **kwargs):
        super(ArticlesForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs["placeholder"] = "Title"
        self.fields["category"].widget.attrs["placeholder"] = "Category"
        self.fields["content"].widget.attrs["placeholder"] = "Content"
        self.fields["picture"].widget.attrs["placeholder"] = "Picture"
        self.fields["tag"].widget.attrs["placeholder"] = "Tag"

        for field in self.fields:
            if field == 'category':
                self.fields[field].widget.attrs['class'] = "form-select"
            elif field == 'tag':
                self.fields[field].widget.attrs['class'] = "form-select"
            else:
                self.fields[field].widget.attrs['class'] = "form-control"
