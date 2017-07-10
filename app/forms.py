from django import forms
from django.forms import ModelForm
from .models import riders,Zone,adm
from django.utils.safestring import mark_safe
from .models import riders,Zone
from crispy_forms.helper import FormHelper
class zoneform(ModelForm):

    class Meta:
        model=Zone
        fields=['name']



class riderform1(ModelForm):

    class Meta:
        model=riders
        fields=['name','phone','zone']


class riderform2(forms.Form):

    file=forms.FileField()

class msgform(forms.Form):   
    
    Select_All_Zones=forms.CharField(widget=forms.CheckboxInput,required=False)
    Zone = forms.ModelChoiceField(queryset=Zone.objects.all(),required=False,)
    message=forms.CharField(max_length=140,widget=forms.Textarea(attrs={'rows':8,'cols':50}))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super(msgform, self).__init__(*args, **kwargs)
    
class msgform1(forms.Form): 
    message=forms.CharField(max_length=140,widget=forms.Textarea(attrs={'rows':8,'cols':50}))

