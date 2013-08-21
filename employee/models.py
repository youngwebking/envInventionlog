from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from employee import helpers
from project.models import Project


JOB_CHOICES = (
	('M', 'Upper Management'),
	('P', 'Production Manager'),
	('D', 'Draftsman'),
	('T', 'Machine Technician'),
	('B', 'Model Builder'),
)

STATUS = (
	('A', 'Available'),
	('U', 'Unavailable'),
)

class Employee(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	slug = models.SlugField(blank=True)
	#username = models.CharField(max_length=8, unique=True)
	job = models.CharField(max_length=1, choices=JOB_CHOICES)
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=50)
	#status = models.CharField(max_length=1, choices=STATUS, default='A')
	
	pic_height=models.PositiveIntegerField(default=100, editable=False)
	pic_width=models.PositiveIntegerField(default=100, editable=False)
	pic = models.ImageField(upload_to="employees/pics", height_field='pic_height', width_field='pic_width', blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		
# create our user object to attach to our player object
#def create_employee_user_callback(sender, instance, **kwargs):
#	employee, new = Employee.objects.get_or_create(user=instance)
#post_save.connect(create_employee_user_callback, User)

class Manager(Employee):
	#assigned = models.CharField(max_length=1, choices=ASSN_CHOICES)
	description = models.TextField(blank=True)
	
	#def approve(project):
		#project.draft.approved = True
	
	def __unicode__(self):
		return self.name

class ProductionManager(Employee):
	description = models.TextField(blank=True)
	projects = models.ForeignKey("project.Project", blank=True, null=True)
	#def approve(project):
		#project.models.draft.approved = True
	
	def __unicode__(self):
		return self.name
		
class Draftsman(Employee):
	description = models.TextField(blank=True)
	productionManager = models.ForeignKey("ProductionManager", blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		
class MachineTechnician(Employee):
	description = models.TextField(blank=True)
	productionManager = models.ForeignKey("ProductionManager", blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		
class ModelBuilder(Employee):
	description = models.TextField(blank=True)
	productionManager = models.ForeignKey("ProductionManager", blank=True, null=True)
	
	def __unicode__(self):
		return self.name
