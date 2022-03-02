from django import forms


class PostCreationForm(forms.Form):
    title=forms.CharField(max_length=225)
    content=forms.CharField(max_length=500)
    author=forms.CharField(max_length=255)
