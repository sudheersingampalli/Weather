from django import forms
from . models import Cities

class Cities_form(forms.ModelForm):
	class Meta:
		model = Cities
		fields = ['City_name']


