from django import forms
import logging
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Teacher, TeacherInfo

logger = logging.getLogger(__name__)

class RegisterForm(UserCreationForm):
    phone = forms.CharField(
        label='Номер телефона'
        )
    birthday = forms.DateField(
        label='Дата рождения',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
        )
    avatar = forms.ImageField(required=False, label='Аватар')

    class Meta:
        model = Teacher
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=commit)
        avatar = self.cleaned_data.get('avatar')
        TeacherInfo.objects.create(
            teacher=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone=self.cleaned_data['phone'],
            birthday=self.cleaned_data.get('birthday'),
            avatar=avatar,
        )
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs['class'] = 'form-control'


class UserUpdateForm(UserChangeForm):
    password = None  # Убираем поле пароля
    
    class Meta:
        model = Teacher
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs['class'] = 'form-control'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = ['phone', 'first_name', 'last_name', 'birthday', 'avatar']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            # Проверяем размер файла (не более 5MB)
            if avatar.size > 5 * 1024 * 1024:
                logger.warning(f"Avatar file too large: {avatar.size} bytes")
                raise forms.ValidationError('Размер файла не должен превышать 5MB')
        return avatar
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs['class'] = 'form-control'
