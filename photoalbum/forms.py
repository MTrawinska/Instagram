from django import forms
from photoalbum.models import *


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['path']

    # def __init__(self, *args, **kwargs):
    #     super().__init__( *args, **kwargs)
    #     self.fields['path'].required = False
