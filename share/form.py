from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Document, UserProfile
from django.contrib.auth.models import User



class CustomCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label = "Password",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2= forms.CharField(
        label= "Confirmez le mot de passe",
        widget= forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip = False,
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']
        
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'email', 'profession']
   
   
        
class PasswordResetEmailForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=254
    )



class PasswordRresetCodeForm(forms.Form):
    code = forms.CharField(label="Code", max_length=4)



class PasswordResetNewPasswordForm(forms.ModelForm):
    password1 = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmez le motde passe", widget=forms.PasswordInput)