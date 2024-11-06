from django import forms
from .models import User,Profile

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

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

