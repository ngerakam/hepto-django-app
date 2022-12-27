from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ChoiceField, EmailInput, FileField, ModelForm, TextInput, Textarea

from .models import Article, ProfileDetails
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ArticlesForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'slug', 'author',
                  'category', 'content', 'picture', 'tag']

    def __init__(self, *args, **kwargs):
        super(ArticlesForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs["placeholder"] = "Title"
        self.fields["slug"].widget.attrs["placeholder"] = "retype-title-with-hyphens"
        self.fields["category"].widget.attrs["placeholder"] = "Category"
        self.fields["content"].widget.attrs["placeholder"] = "Content"
        self.fields["picture"].widget.attrs["placeholder"] = "Picture"
        self.fields["tag"].widget.attrs["placeholder"] = "Tag"

        for field in self.fields:
            if field == 'category':
                self.fields[field].widget.attrs['class'] = "form-select"
            elif field == 'tag':
                self.fields[field].widget.attrs['class'] = "form-select"

            elif field == 'content':
                self.fields[field].widget.attrs['class'] = "form-control"
                self.fields[field].widget.attrs['style'] = "height: 280px"
            else:
                self.fields[field].widget.attrs['class'] = "form-control"


class ProfileDetailForms(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ['city', 'country', 'medical_field', 'detail',
                  'address', 'zip_code', 'gender', 'secondary_phone', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileDetailForms, self).__init__(*args, **kwargs)

        self.fields["city"].widget.attrs["placeholder"] = "City"
        self.fields["country"].widget.attrs["placeholder"] = "County"
        self.fields["address"].widget.attrs["placeholder"] = "Address"
        self.fields["zip_code"].widget.attrs["placeholder"] = "Zip Code"
        self.fields["gender"].widget.attrs["placeholder"] = "Gender"
        self.fields["secondary_phone"].widget.attrs["placeholder"] = "Secondary Phone"
        self.fields["profile_image"].widget.attrs["placeholder"] = "Picture"
        self.fields["medical_field"].widget.attrs["placeholder"] = "Medical area of specialization"
        self.fields["detail"].widget.attrs["placeholder"] = "Tell us about your self"

        for field in self.fields:
            if field == 'gender':
                self.fields[field].widget.attrs['class'] = "form-select"

            elif field == 'detail':
                self.fields[field].widget.attrs['class'] = "form-control"
                self.fields[field].widget.attrs['style'] = "height: 280px"
            else:
                self.fields[field].widget.attrs['class'] = "form-control"
