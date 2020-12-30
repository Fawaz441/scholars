from django import forms
from django.contrib.auth.models import User
# from phonenumber_field.formfields import PhoneNumberField

def validate_password(value):
    if len(value) < 8:
        raise forms.ValidationError(
            ('Password must be up to 8 characters.'),
            params={'value': value},
        )


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=14, required=False,help_text = 'Preferably an active whatsapp number')
    password = forms.CharField(widget=forms.PasswordInput,help_text='Must be up to 8 characters',validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput,validators=[validate_password])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")
        email_query = User.objects.filter(email=email)
        if email_query.exists():
            raise forms.ValidationError("A user with this email already exists!")
        if password1!=password2:
            raise forms.ValidationError("The passwords do not match")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        username_query = User.objects.filter(username=username)
        if not username_query.exists():
            raise forms.ValidationError("{} does not exist ".format(username))





