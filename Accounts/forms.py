from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        password = self.cleaned_data["password1"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial['password']


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(required=True, widget=forms.PasswordInput)


# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput, max_length=555, required=False)
#     password2 = forms.CharField(widget=forms.PasswordInput, max_length=555, required=False,label='Confirm Password')

#     def cleaned_username(self):
#         username = self.cleaned_data('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError('Username is taken')
#         return username

#     def clean_email(self):
#         email = self.cleaned_data('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError('Email is already taken')
#         return email

#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password2 != password:
#             raise forms.ValidationError("passwords must match.")
#         return data
