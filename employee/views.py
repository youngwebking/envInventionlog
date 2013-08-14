from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from employee.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.contrib import messages
from employee import helpers
from employee.models import Employee, Manager, ProductionManager, Draftsman, MachineTechnician, ModelBuilder
from project.models import Project

# REGISTERING -------------------------------------------
def EmployeeRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/profile/")
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['name'], email=form.cleaned_data['email'], password=form.cleaned_data['answer'])
			user.save()
			#employee = user.get_profile()
			#employee.name = form.cleaned_data['name']
			#employee.question = form.cleaned_data['question']
			#employee.answer = form.cleaned_data['answer']
			#employee.job = form.cleaned_data['job']
			#employee.save()
			
			#employee = Employee(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'])
			if form.cleaned_data['job'] == 'M':
				employee = Manager(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'P':
				employee = ProductionManager(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'D':
				employee = Draftsman(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'T':
				employee = MachineTechnician(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'B':
				employee = ModelBuilder(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			name = form.cleaned_data['name']
			answer = form.cleaned_data['answer']
			employee.slug = slugify(name)
			employee.save()
			employee = authenticate(username=name, password=answer)
			if employee is not None:
				login(request, employee)
				if employee.is_authenticated:
					return HttpResponseRedirect('/profile/')
		else:
			return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
	else:
		""" user is not submitting the form, show them a blank registration form """
		form = RegistrationForm()
		context = {'form': form}
		return render_to_response('register.html', context, context_instance=RequestContext(request))
# LOGGING IN-------------------------------------------		
def LoginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			answer = form.cleaned_data['answer']
			employee = authenticate(username=name, password=answer)
			if employee is not None:
				login(request, employee)
				if employee.is_authenticated:
					return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	else:
		""" user is not submitting the form, show the login form """
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance=RequestContext(request))
	
# LOGGING OUT------------------------------------------------	
def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')

# PROFILE PAGE--------------------------------------------
def Profile(request):
	context = None
	if request.user.is_authenticated():
		return render_to_response('profile.html', context, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
	
def SpecificPM(request, pmslug):
	#pm = ProductionManager.objects.get(slug=pmslug)
	projects = Project.objects.filter(productionManager=(user.id-1))
	context = {'pm': pm, 'projects': projects}
	return render_to_response('profile.html', context, context_instance=RequestContext(request))
#UPPPER MANAGEMENT---------------------------------------------------------
def ManagersAll(request):
	managers = Manager.objects.all()
	context = {'managers': managers}
	return render_to_response('../templates/managersall.html', context, context_instance=RequestContext(request))
	
def SpecificManager(request, managerslug):
	try:
		manager = Manager.objects.get(slug=managerslug)
		context = {'manager': manager}
		return render_to_response('singlemanager.html', context, context_instance=RequestContext(request))
	except:
		messages.error(request, 'Try creating a Manager object.')
		raise Http404("It doesn't mind whatever you put here")

# PRODUCTION MANAGER---------------------------------------------------------
def PMsAll(request):
	pms = ProductionManager.objects.all()
	context = {'pms': pms}
	return render_to_response('../templates/pmsall.html', context, context_instance=RequestContext(request))
	
def SpecificPM(request, pmslug):
		pm = ProductionManager.objects.get(slug=pmslug)
		projects = Project.objects.filter(productionManager=pm.id)
		try:
			draftsmen = Draftsman.objects.filter(productionManager=pm.id)
		except:
			draftsmen = None
		try:
			mts = MachineTechnician.objects.filter(productionManager=pm.id)
		except:
			mts = None
		context = {'pm': pm, 'projects': projects, 'draftsmen': draftsmen, 'mts': mts}
		return render_to_response('singlepm.html', context, context_instance=RequestContext(request))
		

# DRAFTSMEN -----------------------------------------------------------------
def DraftsmenAll(request):
	draftsmen = Draftsman.objects.all()
	context = {'draftsmen': draftsmen}
	return render_to_response('../templates/draftsmenall.html', context, context_instance=RequestContext(request))
	
def SpecificDraftsman(request, draftsmanslug):
	try:
		draftsman = Draftsman.objects.get(slug=draftsmanslug)
		projects = Project.objects.filter(draftsman=draftsman.id)
		context = {'draftsman': draftsman, 'projects': projects}
		return render_to_response('singledraftsman.html', context, context_instance=RequestContext(request))
	except:
		messages.error(request, 'That draftsman does not exist!')
		raise Http404("That draftsman does not exist!")

# MACHINE TECHNICIANS ------------------------------------------------------------------
def MTsAll(request):
	mts = MachineTechnician.objects.all()
	context = {'mts': mts}
	return render_to_response('../templates/mtsall.html', context, context_instance=RequestContext(request))
	
def SpecificMT(request, mtslug):
	try:
		mt = MachineTechnician.objects.get(slug=mtslug)
		projects = Project.objects.filter(machineTech=mt.id)
		context = {'mt': mt, 'projects': projects}
		return render_to_response('singlemt.html', context, context_instance=RequestContext(request))
	except:
		messages.error(request, 'That Machine Technician does not exist!')
		raise Http404("That Machine Technician does not exist!")
	
# MODEL BUILDERS ------------------------------------------------------------------
def MBsAll(request):
	mbs = ModelBuilder.objects.all()
	context = {'mbs': mbs}
	return render_to_response('../templates/mbsall.html', context, context_instance=RequestContext(request))
	
def SpecificMB(request, mbslug):
	try:
		mb = ModelBuilder.objects.get(slug=mbslug)
		projects = Project.objects.filter(modelBuilder=mb.id)
		context = {'mb': mb, 'projects': projects}
		return render_to_response('singlemb.html', context, context_instance=RequestContext(request))
	except:
		messages.error(request, 'That Model Builder does not exist!')
		raise Http404("That Model Builder does not exist!")
	
	






	
	
	
