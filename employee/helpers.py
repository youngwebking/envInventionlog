from django.db import models
from django.template.defaultfilters import slugify
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
