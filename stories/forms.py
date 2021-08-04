from django import forms
from stories.models import Contact, Recipe, Story, Subscriber
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your name')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your email')
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Subject')
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Message'),
                'cols': 50,
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError(
                'Daxil edilen email yanliz gmail hesabi olmalidir')
        return email


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = (
            'title',
            'description',
            'image',
            'tags',
            'category',
            'author',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Title')
            }),
            'description': CKEditorUploadingWidget(attrs={
                'class': 'form-control',
                'placeholder': _('Description')
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': _('Tags')
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': _('Select category')
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': _('Author')
            }),
        }


class RecipeForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Recipe
        fields = ('title', 'short_description',
                  'description', 'image', 'category', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Resept Başlığı'),
                
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Qisa Mezmun'),
                
            }),
            'description': CKEditorUploadingWidget(attrs={
                'class': 'form-control',
                'placeholder': _('Mezmun'),
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': _('Category'),
                
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': _('Tags'),
            }),
        }


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter email address')
            }),
        }
