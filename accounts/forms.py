from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'bio',
            'image',
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Username')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Email')
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('First name')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Last name')
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Biography')
            })
        }

# def clean(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise forms.ValidationError('password and confirm password is not same')
    #     return super().clean()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Email')
    }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': _('Password')
    }))


class ChangePasswordFrom(forms.Form):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Old password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'New password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    password3 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Re-enter new password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = User
        fields = (
            'password1',
            'password2',
            'password3',
        )



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'bio', 'image')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('First name'),
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Last name'),
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Email'),
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Biography'),
            }),
        }


        