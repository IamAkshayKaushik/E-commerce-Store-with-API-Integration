from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_authentication.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    date_of_birth = forms.DateField(input_formats=['%d/%m/%Y'])
    email = forms.EmailField()
    # phone_number = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = UserCreationForm.Meta.fields + ('full_name', 'date_of_birth', 'phone_number')
