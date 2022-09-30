from dataclasses import fields
from . models import JobPost, jobrequest, TalentRequest, HireTalentRequest
from django import forms
from django.contrib import messages

class PostJobForm(forms.ModelForm):
    class Meta:
        terms_and_conditions = forms.BooleanField( required=True, disabled=True)
        model = JobPost
        fields = ['area_of_specialization','title','job_desc','budget','terms_and_conditions']
        
        labels = {
            'title': 'Job title',
            'job_desc': 'Describe Your The job you want to post. Ensure you have captured every detail',
            'budget': 'Budget in (ksh)'
        }

    
    
        


class JobProposalForm(forms.ModelForm):
    class Meta:
        model = jobrequest
        fields = ['area_of_specialization','title','proposal', 'your_budget','terms_and_conditions']
    
        labels = {
            'your_budget': 'Your Budget in (ksh)'
        }

class TalentRequestForm(forms.ModelForm):
    class Meta:
        model = TalentRequest
        fields = ['first_name','last_name','email', 'area_of_specialization','job_title','your_info','location', 'phone_number','terms_of_service','terms_and_conditions']


class HireTalentRequestForm(forms.ModelForm):
    
    class Meta:
        model = HireTalentRequest
        fields = ['first_name', 'last_name', 'email','area_of_need','your_specifications','phone_number','location','terms_of_service','terms_and_conditions']

class HireTermsAndConditionForm(forms.ModelForm):
    class Meta:
        model = HireTalentRequest
        fields=['terms_and_conditions',]
        