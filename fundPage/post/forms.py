from django import forms
from .models import post

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields=('title','author','place','body')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'place': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = post
        fields=('title','body')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'place': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }