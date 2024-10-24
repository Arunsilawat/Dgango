from django import forms
from .models import User,Profile

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='_all_'

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='_all_'

# from django import forms
# from .models import User
# from .models import Profile
# class UserForm(forms.ModelForm):
#     class Meta:
#         models=User
#         fields='__all__'

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         models=Profile
#         fields='__all__'

