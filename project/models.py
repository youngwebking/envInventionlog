from django.db import models
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
	startDate = models.DateField(auto_now=False, auto_now_add=True)
	deadline = models.DateField(blank=True, null=True)
	
	#draftUploadDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#draftApproveDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#draftRejectDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#draftUploadDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#draftApproveDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#draftRejectDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#draftUploadDate3 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#draftApproveDate3 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#prototypeUploadDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#prototypeApproveDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#prototypeRejectDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#prototypeUploadDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#prototypeApproveDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#prototypeRejectDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#prototypeUploadDate3 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#prototypeApproveDate3 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#modelUploadDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#modelApproveDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#modelRejectDate = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#modelUploadDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#modelApproveDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#modelRejectDate2 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#modelUploadDate3 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	#modelApproveDate3 = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
	
	#group = models.CharField(max_length=1, choices=GROUP_CHOICES)
	patentImage1 = models.FileField(upload_to=PATENTS, blank=True, null=True)
	patentImage2 = models.FileField(upload_to=PATENTS, blank=True, null=True)
	stl = models.ForeignKey("Stl", blank=True, null=True)
	dxf = models.ForeignKey("Dxf", blank=True, null=True)
	revolve = models.ForeignKey("Revolve", blank=True, null=True)
	modelImgTop = models.ForeignKey("Image", related_name='modelImgTop', blank=True, null=True)
	modelImg34 = models.ForeignKey("Image", related_name='modelImg34', blank=True, null=True)
	modelImgLeft = models.ForeignKey("Image", related_name='modelImgLeft', blank=True, null=True)
	modelImgFront = models.ForeignKey("Image", related_name='modelImgFront', blank=True, null=True)
	modelImgRight = models.ForeignKey("Image", related_name='modelImgRight', blank=True, null=True)
	productionManager = models.ForeignKey("employee.ProductionManager", blank=True, null=True)
	draftsman = models.ForeignKey("employee.Draftsman", blank=True, null=True)
	machineTech = models.ForeignKey("employee.MachineTechnician", blank=True, null=True)
	modelBuilder = models.ForeignKey("employee.ModelBuilder", blank=True, null=True)
	
	percent_complete = models.IntegerField(default=0)
	accepted = models.BooleanField()
	draftApproved = models.BooleanField()
	prototypeApproved = models.BooleanField()
	modelApproved = models.BooleanField()
	finalApproved = models.BooleanField()
	
	def accept_project(self, d, t, b):
		self.draftsman = d
		self.machineTech = t
		self.modelBuilder = b
		self.accepted = True
		self.status = 'I'
		self.percent_complete = 1
		self.save()
	
	def approve_draft(self):
		self.draftApproved = True
		self.percent_complete = 25
		self.save()
		
	def approve_prototype(self):
		self.prototypeApproved = True
		self.percent_complete = 50
		self.save()
		
	def approve_model(self):
		self.modelApproved = True
		self.percent_complete = 75
		self.save()
		
	def final_approve(self):
		self.finalApproved = True
		self.status = 'C'
		self.percent_complete = 100
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
