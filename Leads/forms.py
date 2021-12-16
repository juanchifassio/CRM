from django import forms
from .models import Lead, Agent

class new_lead_Form(forms.ModelForm):

    class Meta:
        model= Lead
        fields= ['first_name','last_name','birthday','address','email','phone','description','agent']


class new_agent_Form(forms.ModelForm):
    
    class Meta:
        model= Agent
        fields=['first_name', 'last_name', 'email']


class lead_update_Form(forms.ModelForm):
    class Meta:
        model=Lead
        fields=['email','phone','address','description','status','agent']


class agent_update_Form(forms.ModelForm):
    
    class Meta:
        model=Agent
        fields=['first_name', 'last_name', 'phone', 'address', 'image']