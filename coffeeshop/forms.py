from django_summernote.widgets import SummernoteWidget
from django import forms
from django.utils.translation import gettext_lazy as _
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
        exclude = ['author', 'approved', 'published']

        widgets = {
            'content': SummernoteWidget(
                attrs={
                    'summernote': {
                        'width': '100%',
                    }
                })
        }

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)
        self.fields['coffee_image'].widget.attrs['class'] = 'form-control-file'
        if author:
            self.fields['author'].initial = author
            self.fields['author'].widget.attrs['disabled'] = True

        # Override the error messages for all fields
        for field in self.fields.values():
            field.error_messages = {
                'required': _('*** This field is required.'),
            }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coffeeshops'] = Review.objects.filter(status=1, approved=True)
        return context
