from django import forms


"""
    UserRegistration
    username
    email
    password
    confirm

    LoginForm
    username
    password

"""



class UserRegistrationForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
