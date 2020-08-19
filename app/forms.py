from django import forms
from app.models import table

class tableform(forms.ModelForm):
	class Meta:
		model = table
		fields = '__all__'