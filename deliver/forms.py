from django import forms
from django.contrib.auth import get_user_model

from .models import Cat, Dipricing


class CatForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ['nameKu', 'nameEg', 'image']

class DipricingForm(forms.ModelForm):
    
    class Meta:
        model = Dipricing
        fields = ['food', 'title', 'price', 'start_date', 'exp_date']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password_repeat']

    def __init__(self, *args, **kwargs):
        self.user_cache = None  # You need to make the user as None initially
        super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_repeat")
        email = cleaned_data.get('email')

        if get_user_model().objects.filter(email=username).exists():
            self.add_error('email', "ناوت دووبارەیە")

        if get_user_model().objects.filter(email=email).exists():
            self.add_error('email', "ئیمەیڵەکەت دووبارەیە")

        if password != confirm_password:
            self.add_error('password_repeat', "تێپەڕەوشە وەکو یەک نییە")

        return cleaned_data

    def get_user(self):
        return self.user_cache

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

