from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    #Es necesario hacer un override para conseguir cambiar el password
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = '* Contraseña'
        self.fields['password2'].label = '* Confirmar contraseña'

        self.fields['password1'].help_text = 'Debe contener al menos 8 caracteres (letras y números)'
        self.fields['password2'].help_text = 'Introduzca la misma contraseña que la anterior para confirmarla'

    def clean_email(self):
        email = self.cleaned_data['email']
        if email != "":
            if User.objects.filter(email=email).exists():
                raise ValidationError("Ya hay un usuario en el sistema con ese email")
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # Cambiamos label y textos de ayuda de los campos para que se muestren como realmente queremos en nuestro html
        labels = {
            "username": "* Nombre de usuario",
            "email": "Email",
            "first_name": "* Nombre",
            "last_name": "* Apellidos",
        }
        help_texts = {
            "username": "",
        }

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username != "" and username!=self.cleaned_data['username']:
            if User.objects.filter(username=username).exists():
                raise ValidationError("Ya hay un usuario en el sistema con ese nombre de usuario")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email != "" and email!=self.cleaned_data['email']:
            if User.objects.filter(email=email).exists():
                raise ValidationError("Ya hay un usuario en el sistema con ese email")
        return email

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name')