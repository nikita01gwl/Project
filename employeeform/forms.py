from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import employee
from django.conf import settings
from crispy_forms.helper import FormHelper







class employeeform(ModelForm):
    class Meta:
        model=employee
        fields=['Name','Adhaar','Licence_Number','RC_Card_No','Mobile_No','Current_Address','Permanent_Address','Father_spouse_Name','Address','Employee_Id','Hub','Date_of_Joining','Role']

        

class employeeform1(forms.Form):
    
    Enter_Employee_Id = forms.ModelChoiceField(queryset=employee.objects.all(),required=False)

    
    



