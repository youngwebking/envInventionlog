from django.template.defaultfilters import slugify
from django import template

register = template.Library()

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

