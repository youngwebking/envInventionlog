from django.db import models
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect

def redirect_to_profile(request):
	name = request.user.username
	slug = slugify(name)
	if request.user.employee.job == 'P':
		return True
		return HttpResponseRedirect("/production-managers/" + slug)
	elif request.user.employee.job == 'D':
		return HttpResponseRedirect("/draftsmen/" + slug)
	elif request.user.employee.job == 'T':
		return HttpResponseRedirect("/machine-technicians/" + slug)
	elif request.user.employee.job == 'B':
		return HttpResponseRedirect("/model-builders/" + slug)
	return HttpResponseRedirect("/production-managers/" + slug)
	
def get_profile_link(request):
	name = request.user.username
	slug = slugify(name)
	if request.user.employee.job == 'P':
		profile = "/employees/production-managers/" + slug
		return profile
	elif request.user.employee.job == 'D':
		profile = "/employees/draftsmen/" + slug
		return profile
	elif request.user.employee.job == 'T':
		profile = "/machine-technicians/" + slug
		return profile
	elif request.user.employee.job == 'B':
		profile = "/employees/model-builders/" + slug
		return profile
		
def get_template_profile_link(name):
	slug = slugify(name)
	if user.employee.job == 'P':
		profile = "/employees/production-managers/" + slug
		return profile
	elif user.employee.job == 'D':
		profile = "/employees/draftsmen/" + slug
		return profile
	elif user.employee.job == 'T':
		profile = "/machine-technicians/" + slug
		return profile
	elif user.employee.job == 'B':
		profile = "/employees/model-builders/" + slug
		return profile
