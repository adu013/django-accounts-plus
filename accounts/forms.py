from django.contrib.auth import get_user_model
from django.db.models import Q
from django import forms


User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='password confirmation', widget=forms.PasswordInput)
    referral_code = forms.CharField(label='Referral Code', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password do not match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    query = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-field-username'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-field-password'
            }
        )
    )

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_querystring_final = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()
        if not user_querystring_final.exists() and user_querystring_final != 1:
            raise forms.ValidationError(
                "Either Invalid credentials or User do not exists")
        user_obj = user_querystring_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError(
                "Credentials are not correct")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)
