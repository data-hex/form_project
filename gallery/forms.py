#from django.forms import forms
from django import forms
from .models import Gallery


# class GalleryUploadForm(forms.Form):
#     image = forms.FileField()


class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'