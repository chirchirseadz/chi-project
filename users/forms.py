from django import forms
from django.contrib.auth.models import User

from . models import user_profile
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff',)
     

        
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
            'is_staff' : 'Register As Employer',
            'first_name': 'First Name'
        }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]

class EmployeeProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ['national_id','area_of_specialization','job_title','brief_info','address','phone','current_location','image','profile_updated']
        labels = {
            'area_of_specialization': 'Select Area of Specialization',
            'brief_info': 'Talk About Yourself',
            'profile_updated': 'Updated completed'
        }

class EmployerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ['national_id','area_of_specialization','job_title','brief_info','address','phone','current_location','company_name','company_email','image','profile_updated']

        labels = {
            'area_of_specialization': 'Select Area of Specialization',
            'brief_info': 'About Yourself',
            'profile_updated': 'Update completed ?'
        }


