from django.db import models
from django.template.defaultfilters import slugify
from employee.models import Draftsman, MachineTechnician, ModelBuilder
from project.models import Project

def get_random_employee(job):
	if job == "D":
		employees = Draftsman.objects.all()
	elif job == "T":
		employees = MachineTechnician.objects.all()
	elif job == "B":
		employees = ModelBuilder.objects.all()
	employee = employees.order_by('?')[0]
	return employee
	
def get_next_employee(job):
	employee = None
	least = 100
	if job == "D":
		draftsmen = Draftsman.objects.all()
		for draftsman in draftsmen:
			projects = Project.objects.filter(draftsman=draftsman)
			projects = projects.filter(finalApproved=False)
			count = projects.count()
			if count < least and draftsman.status == 'A':
				least = count
				employee = draftsman
			
	elif job == "T":
		mts = MachineTechnician.objects.all()
		for mt in mts:
			projects = Project.objects.filter(machineTech=mt)
			projects = projects.filter(finalApproved=False)
			count = projects.count()
			if count < least and mt.status == 'A':
				least = count
				employee = mt
		
	elif job == "B":
		mbs = ModelBuilder.objects.all()
		for mb in mbs:
			projects = Project.objects.filter(modelBuilder=mb)
			projects = projects.filter(finalApproved=False)
			count = projects.count()
			if count < least and mb.status == 'A':
				least = count
				employee = mb
	return employee

from django import template
register = template.Library()

def get_profile_link(request):
	username = request.user.username
	slug = slugify(username)
	profile = None
	if request.user.employee.job == 'M':
		profile = "/employees/upper-management/" + slug
	elif request.user.employee.job == 'P':
		profile = "/employees/production-managers/" + slug
	elif request.user.employee.job == 'D':
		profile = "/employees/draftsmen/" + slug
	elif request.user.employee.job == 'T':
		profile = "/employees/machine-technicians/" + slug
	elif request.user.employee.job == 'B':
		profile = "/employees/model-builders/" + slug
	if profile != None:
		return profile
