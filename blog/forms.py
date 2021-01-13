from django import forms
from tinymce import TinyMCE
from .models import Post

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostFrom(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols':30, 'rows':10}
        )
    )

    class Meta:
        model = Post
        fields = '__all__'