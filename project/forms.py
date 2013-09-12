from django import forms
from django.forms import ModelForm
from project.models import Project
	
class UploadDraftForm(forms.Form):

	stl = forms.FileField(required=False)
	dxf = forms.FileField(required=False)
	
class UploadModelForm(forms.Form):

	topView = forms.ImageField(required=False)
	View34 = forms.ImageField(required=False)
	leftView = forms.ImageField(required=False)
	frontView = forms.ImageField(required=False)
	rightView = forms.ImageField(required=False)
