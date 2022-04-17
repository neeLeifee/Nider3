from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=100, label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=100, label='Подтверждение пароля:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Логин:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class ProfileForm(forms.Form):
    GENDERS = (
        ('Женский', 'Женский'),
        ('Мужской', 'Мужской'),
        ('Булщит', 'Булщит'),
        ('Боевой вертолёт Ка-52 «Аллигатор»', 'Боевой вертолёт Ка-52 «Аллигатор»'),
    )

    city = forms.CharField(max_length=100, label='Город', widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='Пол', choices=GENDERS, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
