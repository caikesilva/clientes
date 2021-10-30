from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        label = 'Arquivo',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                
            }
        )
    )