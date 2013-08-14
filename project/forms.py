from django import forms
from django.forms import ModelForm
from project.models import Project
	
class UploadDraftForm(forms.Form):
	#stlname = forms.CharField(max_length=50)
	stl = forms.FileField(required=False)
	
	#dxfname = forms.CharField(max_length=50)
	dxf = forms.FileField(required=False)
	
class UploadModelForm(forms.Form):
	#topname = forms.CharField(max_length=50)
	topView = forms.ImageField(required=False)
	
	#rightname = forms.CharField(max_length=50)
	rightView = forms.ImageField(required=False)
	
	#frontname = forms.CharField(max_length=50)
	frontView = forms.ImageField(required=False)
