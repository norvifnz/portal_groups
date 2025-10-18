from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'description', 'material_type', 'file', 'image', 'link']
        widgets = {
            'link': forms.URLInput(attrs={'style': 'display:none;', 'id': 'id_link'}),
        }
