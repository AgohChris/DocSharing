from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Document, UserProfile



# class CustomCreationForm(UserCreationForm):
    
#     password1 = forms.CharField(
#         label = "Password",
#         strip = False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#     )
#     password2= forms.CharField(
#         label= "Confirmez le mot de passe",
#         widget= forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         strip = False,
#     )
    
#     class Meta:
#         fields = []



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']
        
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'email', 'profession']