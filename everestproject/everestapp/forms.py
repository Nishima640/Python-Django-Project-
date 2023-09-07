from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

class ClientNewsCreateForm(forms.ModelForm):
    class Meta:
        model = News 
        fields = "__all__"
        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(),
            'content': SummernoteWidget(attrs={
                'summernote':{
                    'class':'form-control form-control-rounded',
                    'placeholder': 'Page Description',
                }
            }),
            'image' : forms.ClearableFileInput(),

        }

class AdminLoginForm(forms.Form):
    username =  forms.CharField(widget=forms.TimeInput(attrs={
        'class' : 'form-control',
        'placeholder': "username...",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your password..."
     }))


