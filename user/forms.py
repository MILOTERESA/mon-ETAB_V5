from django import forms

from .models.role_user import  RoleUserModel
from .models.user import CustomUserModel


class UsersForm(forms.Form):   
    pseudo = forms.CharField(max_length=10)
    mot_de_passe = forms.CharField(max_length=128)
    confirmer_mot_de_passe= forms.CharField(max_length=255)

class MyUserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields ='__all__'  # Spécifie les champs à inclure dans le formulaire 
        

class RoleUserForm(forms.ModelForm):
    class Meta:
        model = RoleUserModel
        fields = ['role_user']  # Spécifie les champs à inclure dans le formulaire 



  # Spécifie les champs à inclure dans le formulaire                 
                