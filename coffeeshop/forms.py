from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Review

# Form as ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ['author', 'approved', 'published']  # Exclude the author field from the form

        widgets = {
            'content': SummernoteWidget(
                attrs={
                    'summernote': {
                        'width': '100%',
                    }
                })
        }

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)  # Get the current author
        super().__init__(*args, **kwargs)
        self.fields['coffee_image'].widget.attrs['class'] = 'form-control-file'
        if author:
            self.fields['author'].initial = author  # Set the initial value for the author field
            self.fields['author'].widget.attrs['disabled'] = True  # Disable the author field