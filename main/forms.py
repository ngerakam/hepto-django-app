from django.forms import ChoiceField, EmailInput, FileField, ModelForm, TextInput, Textarea

from .models import Volunteer


# volunteer form

class VolunteerForm(ModelForm):

    class Meta:
        model = Volunteer
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["placeholder"] = "Fullname"
        self.fields["email"].widget.attrs["placeholder"] = "Email"

        for field in self.fields:

            self.fields[field].widget.attrs['class'] = "form-control"
