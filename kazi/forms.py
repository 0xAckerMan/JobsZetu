from django import forms
from .models import Candidate, JobList, Company, JobCategory, BackgroundData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class JobListForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = '__all__'




class BackgroundDataForm(forms.ModelForm):
    class Meta:
        model = BackgroundData
        fields = '__all__'

