from django import forms
from .models import Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Reviewfields = "__all__"
