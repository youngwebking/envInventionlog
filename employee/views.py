from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from employee.forms import RegistrationForm, LoginForm1, LoginForm2
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.contrib import messages
from employee.helpers import redirect_to_profile, get_profile_link
from employee.models import Employee, Manager, ProductionManager, Draftsman, MachineTechnician, ModelBuilder
from project.models import Project
import MySQLdb
import _mysql

# HELPERS


# REGISTERING -------------------------------------------
def EmployeeRegistration(request):
	if request.user.is_authenticated():
		#return HttpResponseRedirect("/profile/")
		return HttpResponseRedirect(get_profile_link(request))
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
					#return HttpResponseRedirect("/profile/")
					return HttpResponseRedirect(get_profile_link(request))
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
		#return HttpResponseRedirect("/profile/")
		return HttpResponseRedirect(get_profile_link(request))
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			answer = form.cleaned_data['answer']
			employee = authenticate(username=name, password=answer)
			if employee is not None:
				login(request, employee)
				if employee.is_authenticated:
					#return HttpResponseRedirect("/profile/")
					return HttpResponseRedirect(get_profile_link(request))
			else:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	else:
		""" user is not submitting the form, show the login form """
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance=RequestContext(request))
	
def Login(request, nameslug):
	if request.user.is_authenticated():
		#return HttpResponseRedirect("/profile/")
		return HttpResponseRedirect(get_profile_link(request))
	if request.method == 'POST':
		if nameslug == '':
			form = LoginForm1(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				nameslug = slugify(name)
				return HttpResponseRedirect('/login/' + nameslug)
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			form = LoginForm2(request.POST)
			if form.is_valid():
				employee = Employee.objects.get(slug=nameslug)
				name = employee.name
				answer = form.cleaned_data['answer']
				employee = authenticate(username=name, password=answer)
				if employee is not None:
					login(request, employee)
					if employee.is_authenticated:
						#return HttpResponseRedirect("/profile/")
						return HttpResponseRedirect(get_profile_link(request))
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	else:
		""" user is not submitting the form, show the login form """
		if nameslug == '':
			form = LoginForm1()
			context = {'form': form}
			return render_to_response('login.html', context, context_instance=RequestContext(request))
		else:
			employee = Employee.objects.get(slug=nameslug)
			form = LoginForm2()
			context = {'form': form, 'employee': employee}
			return render_to_response('login2.html', context, context_instance=RequestContext(request))

# LOGGING OUT------------------------------------------------	
def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')

# PROFILE PAGE--------------------------------------------
def Profile(request):
	if request.user.is_authenticated():
		name = request.user.username
		if request.user.employee.job == 'P':
			pm = ProductionManager.objects.get(name=name)
			#projects = Project.objects.filter(productionManager=pm.id)
		elif request.user.employee.job == 'D':
		#	projects = Project.objects.filter(draftsman.name=name)
			pass
		elif request.user.employee.job == 'T':
		#	projects = Project.objects.filter(machineTech.name=name)
			pass
		elif request.user.employee.job == 'B':
		#	projects = Project.objects.filter(modelBuilder.name=name)
			pass
		#context = {'projects': projects}
		context = None
		if request.method == 'POST':
			try:
				conn = MySQLdb.connect('localhost', 'root', 'chewy')
				with conn:
					cur = conn.cursor()
					cur.execute("USE projects")
					cur.execute("SELECT project_name FROM projects WHERE assigned='False'")
					result = cur.fetchone()
					project_name = `result`[2:-3]
					cur.execute("SELECT patent_number FROM projects WHERE project_name='" + project_name + "'")
					result2 = cur.fetchone()
					patent_number = `result2`[1:-3]
					cur.execute ("UPDATE projects SET assigned='True' WHERE project_name='%s' " % (project_name))
					
					slug = slugify(project_name)
					project = Project(name=project_name, slug=slug, number=patent_number, status="I", productionManager=pm)
					project.save()
			
			except _mysql.Error, e:
			  	print "Error %d: %s" % (e.args[0], e.args[1])
				sys.exit(1)

			finally:
				if conn:
					conn.close()
		return render_to_response('profile.html', context, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
	
#def SpecificPM(request, pmslug):
#	#pm = ProductionManager.objects.get(slug=pmslug)
#	projects = Project.objects.filter(productionManager=(user.id-1))
#	context = {'pm': pm, 'projects': projects}
#	return render_to_response('profile.html', context, context_instance=RequestContext(request))
	

#UPPER MANAGEMENT---------------------------------------------------------
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
		if slugify(request.user.username) == pmslug:
			if request.method == 'POST':
				try:
					conn = MySQLdb.connect('localhost', 'root', 'chewy')
					with conn:
						cur = conn.cursor()
						cur.execute("USE projects")
						cur.execute("SELECT project_name FROM projects WHERE assigned='False'")
						result = cur.fetchone()
						project_name = `result`[2:-3]
						cur.execute("SELECT patent_number FROM projects WHERE project_name='" + project_name + "'")
						result2 = cur.fetchone()
						patent_number = `result2`[1:-3]
						cur.execute ("UPDATE projects SET assigned='True' WHERE project_name='%s' " % (project_name))
					
						slug = slugify(project_name)
						project = Project(name=project_name, slug=slug, number=patent_number, status="I", productionManager=pm)
						project.save()
			
				except _mysql.Error, e:
				  	print "Error %d: %s" % (e.args[0], e.args[1])
					sys.exit(1)

				finally:
					if conn:
						conn.close()
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
	
	






	
	
	
