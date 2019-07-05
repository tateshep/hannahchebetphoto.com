from django import forms
from .models import Image, Collection

class UploadPhotoForm(forms.ModelForm):
    # A photo upload form used in the NewImage View
    class Meta:
        model = Image
        fields = ['title','photo']
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    # 'class' : 'file-input',
                    'multiple': True
                }
            )
        }

