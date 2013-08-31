from django.db import models
from project import helpers
from django.core.files.storage import FileSystemStorage

PATENTS  = "pics/patents"
DRAFTS   = "pics/drafts"
MODELS   = "pics/models"
REVOLVES = "revolves"

STATUS = (
	('C', 'Complete'),
	('P', 'Pending'),
	('I', 'In Progress'),
)

class Project(models.Model):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(blank=True)
	number = models.IntegerField(blank=True)
	status = models.CharField(max_length=1, choices=STATUS)
	#deadline = models.DateField()
	#group = models.CharField(max_length=1, choices=GROUP_CHOICES)
	patentImage1 = models.FileField(upload_to=PATENTS, blank=True, null=True)
	patentImage2 = models.FileField(upload_to=PATENTS, blank=True, null=True)
	stl = models.ForeignKey("Stl", blank=True, null=True)
	dxf = models.ForeignKey("Dxf", blank=True, null=True)
	revolve = models.ForeignKey("Revolve", blank=True, null=True)
	modelImgTop = models.ForeignKey("Image", related_name='modelImgTop', blank=True, null=True)
	modelImgRight = models.ForeignKey("Image", related_name='modelImgRight', blank=True, null=True)
	modelImgFront = models.ForeignKey("Image", related_name='modelImgFront', blank=True, null=True)
	
	productionManager = models.ForeignKey("employee.ProductionManager", blank=True, null=True)
	draftsman = models.ForeignKey("employee.Draftsman", blank=True, null=True)
	machineTech = models.ForeignKey("employee.MachineTechnician", blank=True, null=True)
	modelBuilder = models.ForeignKey("employee.ModelBuilder", blank=True, null=True)
	
	percent_complete = models.IntegerField(default=0)
	draftApproved = models.BooleanField()
	modelApproved = models.BooleanField()
	
	def approve_draft(self):
		self.draftApproved = True
		self.save()
		
	def approve_model(self):
		self.modelApproved = True
		self.save()
	
	def __unicode__(self):
		return self.name

class Stl(models.Model):
	#name = models.CharField(max_length=50, unique=True)
	#slug = models.SlugField(blank=True)
	stl = models.FileField(upload_to=DRAFTS)
	
	#def __unicode__(self):
		#return self.name
		
class Dxf(models.Model):
	#name = models.CharField(max_length=50, unique=True)
	#slug = models.SlugField(blank=True)
	dxf = models.FileField(upload_to=DRAFTS)
	
	#def __unicode__(self):
		#return self.name
		
class Image(models.Model):
	#name = models.CharField(max_length=50, unique=True)
	image = models.ImageField(upload_to=MODELS)
	
	#def __unicode__(self):
		#return self.name

class Revolve(models.Model):
	#name = models.CharField(max_length=50, unique=True)
	revolve = models.FileField(upload_to=REVOLVES)
	
	#def __unicode__(self):
		#return self.name
