# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Course

# create a ModelForm
class Form(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Course
		fields = "__all__"
