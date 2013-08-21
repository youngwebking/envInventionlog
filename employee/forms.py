from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from employee.models import Employee

JOB_CHOICES = (
	('M', 'Upper Management'),
	('P', 'Production Manager'),
	('D', 'Draftsman'),
	('T', 'Machine Technician'),
	('B', 'Model Builder'),
)

class RegistrationForm(ModelForm):
	name = forms.CharField(label=(u'Name'))
	email = forms.EmailField(label=(u'Email Address'))
	question = forms.CharField(label=(u'Question'))
	answer = forms.CharField(label=(u'Answer'))
	job = forms.ChoiceField(label=(u'Job'), choices=JOB_CHOICES)
	pic = forms.ImageField(label=(u'Profile Picture'), required=False)
	
	class Meta:
		model = Employee
		exclude = ('user',)
		
class LoginForm(forms.Form):
	name = forms.CharField(label=(u'Name'))
	
	#employee = Employee.objects.get(name=name)
	#question = employee.question
	answer = forms.CharField(label=(u'Answer'), widget=forms.PasswordInput(render_value=False))
	
class LoginForm1(forms.Form):
	name = forms.CharField(label=(u'Name'))

class LoginForm2(forms.Form):
	answer = forms.CharField(label=(u'Answer'), widget=forms.PasswordInput(render_value=False))
