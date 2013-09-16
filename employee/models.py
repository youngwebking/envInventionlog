from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from project.models import Project


JOB_CHOICES = (
	('M', 'Upper Management'),
	('P', 'Production Manager'),
	('D', 'Draftsman'),
	('T', 'Machine Technician'),
	('B', 'Model Builder'),
	('A', 'Admin'),
)

STATUS = (
	('A', 'Available'),
	('U', 'Unavailable'),
)

class Employee(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	slug = models.SlugField(blank=True)
	username = models.CharField(max_length=20, unique=True)
	job = models.CharField(max_length=1, choices=JOB_CHOICES)
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=50)
	status = models.CharField(max_length=1, choices=STATUS, default='A')
	rating = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
	
	pic_height=models.PositiveIntegerField(default=100, editable=False)
	pic_width=models.PositiveIntegerField(default=100, editable=False)
	pic = models.ImageField(upload_to="employees/pics", blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		
# create our user object to attach to our player object
#def create_employee_user_callback(sender, instance, **kwargs):
#	employee, new = Employee.objects.get_or_create(user=instance)
#post_save.connect(create_employee_user_callback, User)

class Manager(Employee):
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class ProductionManager(Employee):
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name
		
class Draftsman(Employee):
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name
		
class MachineTechnician(Employee):
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name
		
class ModelBuilder(Employee):
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name
