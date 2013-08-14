from project import helpers
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.defaultfilters import slugify
from project.models import Project, Stl, Dxf, Image
from project.forms import UploadDraftForm, UploadModelForm

# UPLOAD DRAFT FILES------------------------------------------------------------------
def upload_draft(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if request.user.is_authenticated():
		if request.user.username == project.draftsman.name:
			if request.method == 'POST':
				form = UploadDraftForm(request.POST, request.FILES)
				if form.is_valid():
					newstl = Stl(stl=request.FILES['stl'])
					newstl.save()
					
					newdxf = Dxf(dxf=request.FILES['dxf'])
					newdxf.save()
					
					project = Project.objects.get(slug=projectslug)
					project.stl = newstl
					project.dxf = newdxf
					project.save()
					return HttpResponseRedirect('/projects/' + projectslug + '/')
				else:
					form = UploadDraftForm()
					context = {'form': form, 'project': project}
					return render_to_response('upload-draft.html', context, context_instance=RequestContext(request))
			else:
				form = UploadDraftForm()
				context = {'form': form, 'project': project}
				return render_to_response('upload-draft.html', context, context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
# UPLOAD MODEL IMAGES----------------------------------------------------		
def upload_model(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if request.user.is_authenticated():
		if request.user.username == project.modelBuilder.name:
			if request.method == 'POST':
				form = UploadModelForm(request.POST, request.FILES)
				if form.is_valid():
					newtop = Image(image=request.FILES['topView'])
					newtop.save()
					
					newright = Image(image=request.FILES['rightView'])
					newright.save()
					
					frontname = form.cleaned_data['frontView']
					newfront = Image(image=request.FILES['frontView'])
					newfront.save()
					
					project = Project.objects.get(slug=projectslug)
					project.modelImgTop = newtop
					project.modelImgRight = newright
					project.modelImgFront = newfront
					project.save()
					return HttpResponseRedirect('/projects/' + projectslug + '/')
				else:
					form = UploadModelForm()
					context = {'form': form, 'project': project}
					return render_to_response('upload-model.html', context, context_instance=RequestContext(request))
			else:
				form = UploadModelForm()
				context = {'form': form, 'project': project}
				return render_to_response('upload-model.html', context, context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

# PROJECTS-------------------------------------
def ProjectsAll(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render_to_response('../templates/projectsall.html', context, context_instance=RequestContext(request))
	
def SpecificProject(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	context = {'project': project}
	return render_to_response('singleproject.html', context, context_instance=RequestContext(request))
