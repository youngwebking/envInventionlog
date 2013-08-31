from django.template.defaultfilters import slugify
from django import template

register = template.Library()

def get_template_profile_link_dud():
	#user = request.user
	username = user.username
	slug = slugify(username)
	profile = None
	if user.employee.job == 'M':
		profile = "/employees/upper-management/" + slug
	elif user.employee.job == 'P':
		profile = "/employees/production-managers/" + slug
	elif user.employee.job == 'D':
		profile = "/employees/draftsmen/" + slug
	elif user.employee.job == 'T':
		profile = "/employees/machine-technicians/" + slug
	elif user.employee.job == 'B':
		profile = "/employees/model-builders/" + slug
	if profile != None:
		return profile

@register.simple_tag
def get_template_profile_link(username, job):
	profile = None
	if job == 'M':
		profile = "/employees/upper-management/" + username
	elif job == 'P':
		profile = "/employees/production-managers/" + username
	elif job == 'D':
		profile = "/employees/draftsmen/" + username
	elif job == 'T':
		profile = "/employees/machine-technicians/" + username
	elif job == 'B':
		profile = "/employees/model-builders/" + username
	if profile != None:
		return profile
		
#register.tag('get_template_profile_link', get_template_profile_link)



@register.simple_tag
def print_hello():
	return "hello"

