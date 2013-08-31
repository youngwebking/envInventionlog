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
	name = forms.CharField(label=(u'Name'), widget=forms.TextInput(attrs={'placeholder': 'ex: John Smith'}))
	email = forms.EmailField(label=(u'Email Address'))
	question = forms.CharField(label=(u'Question'))
	answer = forms.CharField(label=(u'Answer'))
	job = forms.ChoiceField(label=(u'Job'), choices=JOB_CHOICES)
	pic = forms.ImageField(label=(u'Profile Picture'), required=False)
	
	class Meta:
		model = Employee
		exclude = ('user', 'username', 'status', 'rating',)
		
class LoginForm(forms.Form):
	username = forms.CharField(label=(u'Username'), widget=forms.TextInput(attrs={'placeholder': 'ex: john0087'}))
	
	#employee = Employee.objects.get(name=name)
	#question = employee.question
	answer = forms.CharField(label=(u'Answer'), widget=forms.PasswordInput(render_value=False))
	
class LoginForm1(forms.Form):
	username = forms.CharField(label=(u'Username'))

class LoginForm2(forms.Form):
	answer = forms.CharField(label=(u'Answer'), widget=forms.PasswordInput(render_value=False))
