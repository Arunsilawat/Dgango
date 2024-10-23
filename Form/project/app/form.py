from django import form
from.models import User
from.models import Profile
class UserForm(forms.ModelForm):
    class Meta:
        models=User
        fields='__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        models=Profile
        fields='__all__'