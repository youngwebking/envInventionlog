from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from employee.forms import RegistrationForm, LoginForm1, LoginForm2
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.contrib import messages
from employee.helpers import get_profile_link
from employee.models import Employee, Manager, ProductionManager, Draftsman, MachineTechnician, ModelBuilder
from project.models import Project
from django import template
import MySQLdb
import _mysql
import re

# HELPERS

# REGISTERING -------------------------------------------
def EmployeeRegistration(request):
	if request.user.is_authenticated():
		#return HttpResponseRedirect("/profile/")
		return HttpResponseRedirect(get_profile_link(request))
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			try:
				conn = MySQLdb.connect('localhost', 'root', 'chewy')
				cur = conn.cursor()
				cur.execute("USE inventionlog")
				cur.execute("SELECT COUNT(*) FROM auth_user")
				result = cur.fetchone()
				num_rows = result[0]
			
			except _mysql.Error, e:
			  	print "Error %d: %s" % (e.args[0], e.args[1])
				sys.exit(1)

			finally:
				if conn:
					conn.close()
			num_rows = `num_rows`[:-1]
			i = 0
			for digit in num_rows:
				i += 1
			if i == 1:
				userid = '000' + num_rows
			elif i == 2:
				userid = '00' + num_rows
			elif i == 3:
				userid = '0' + num_rows
			elif i == 4:
				userid = num_rows
				
			name = form.cleaned_data['name']
			fname = re.sub(r'\ .*', '', name)
			username = slugify(fname) + userid
			answer = form.cleaned_data['answer']
			answer = slugify(answer)
			user = User.objects.create_user(username=username, email=form.cleaned_data['email'], password=answer)
			user.save()
			#employee = user.get_profile()
			#employee.username = form.cleaned_data['name']
			#employee.question = form.cleaned_data['question']
			#employee.answer = form.cleaned_data['answer']
			#employee.job = form.cleaned_data['job']
			#employee.save()
			
			#employee = Employee(user=user, name=form.cleaned_data['name'], question=form.cleaned_data['question'], answer=form.cleaned_data['answer'], job=form.cleaned_data['job'])
			if form.cleaned_data['job'] == 'M':
				employee = Manager(user=user, name=name, username=username, question=form.cleaned_data['question'], answer=answer, job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'P':
				employee = ProductionManager(user=user, name=name, username=username, question=form.cleaned_data['question'], answer=answer, job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'D':
				employee = Draftsman(user=user, name=name, username=username, question=form.cleaned_data['question'], answer=answer, job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'T':
				employee = MachineTechnician(user=user, name=name, username=username, question=form.cleaned_data['question'], answer=answer, job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			elif form.cleaned_data['job'] == 'B':
				employee = ModelBuilder(user=user, name=name, username=username, question=form.cleaned_data['question'], answer=answer, job=form.cleaned_data['job'], pic=form.cleaned_data['pic'])
			employee.slug = slugify(name)
			employee.save()
			employee = authenticate(username=username, password=answer)
			if employee is not None:
				login(request, employee)
				if employee.is_authenticated:
					#return HttpResponseRedirect("/profile/")
					profile = get_profile_link(request)
					messages.add_message(request, messages.SUCCESS, 'Your account has been successfully activated! Your username is: ' + username + '.')
					return HttpResponseRedirect(get_profile_link(request))
		else:
			return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
	else:
		""" user is not submitting the form, show them a blank registration form """
		form = RegistrationForm()
		context = {'form': form}
		return render_to_response('register.html', context, context_instance=RequestContext(request))
# LOGGING IN-------------------------------------------
	
def Login(request, username):
	if request.user.is_authenticated():
		#return HttpResponseRedirect("/profile/")
		return HttpResponseRedirect(get_profile_link(request))
	if request.method == 'POST':
		if username == '':
			form = LoginForm1(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				username = slugify(username)
				return HttpResponseRedirect('/login/' + username)
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			form = LoginForm2(request.POST)
			if form.is_valid():
				employee = Employee.objects.get(username=username)
				username = employee.username
				answer = form.cleaned_data['answer']
				employee = authenticate(username=slugify(username), password=slugify(answer))
				if employee is not None:
					login(request, employee)
					if employee.is_authenticated:
						#return HttpResponseRedirect("/profile/")
						profile = get_profile_link(request)
						messages.add_message(request, messages.SUCCESS, 'You have been successfully logged in!')
						return HttpResponseRedirect(get_profile_link(request))
			return HttpResponseRedirect('/login/')
	else:
		""" user is not submitting the form, show the login form """
		if username == '':
			form = LoginForm1()
			context = {'form': form}
			return render_to_response('login.html', context, context_instance=RequestContext(request))
		else:
			employee = Employee.objects.get(username=username)
			form = LoginForm2()
			context = {'form': form, 'employee': employee}
			return render_to_response('login2.html', context, context_instance=RequestContext(request))

# LOGGING OUT------------------------------------------------	
def LogoutRequest(request):
	messages.add_message(request, messages.SUCCESS, 'You have been successfully logged out.')
	logout(request)
	return HttpResponseRedirect('/')

#UPPER MANAGEMENT---------------------------------------------------------
def ManagersAll(request):
	managers = Manager.objects.all()
	context = {'managers': managers}
	return render_to_response('../templates/managersall.html', context, context_instance=RequestContext(request))
	
def SpecificManager(request, username):
	employee = Employee.objects.get(username=username)
	try:
		manager = Manager.objects.get(username=username)
		context = {'manager': manager}
	except:
		messages.error(request, 'That manager does not exist!')
		raise Http404("That manager does not exist!")
	return render_to_response('singlemanager.html', context, context_instance=RequestContext(request))

# PRODUCTION MANAGER---------------------------------------------------------
def PMsAll(request):
	pms = ProductionManager.objects.all()
	context = {'pms': pms}
	return render_to_response('../templates/pmsall.html', context, context_instance=RequestContext(request))
	
def SpecificPM(request, username):
	try:
		employee = Employee.objects.get(username=username)
		pm = ProductionManager.objects.get(username=username)
		projects = Project.objects.filter(productionManager=pm.id)
	except:
		messages.error(request, 'That production manager does not exist!')
		raise Http404("That production manager does not exist!")
	if slugify(request.user.username) == username:
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
					project = Project(name=project_name, slug=slug, number=patent_number, status="P", productionManager=pm)
					project.save()
			
			except _mysql.Error, e:
			  	print "Error %d: %s" % (e.args[0], e.args[1])
				sys.exit(1)

			finally:
				if conn:
					conn.close()
	context = {'pm': pm, 'employee': employee, 'projects': projects}
	return render_to_response('singlepm.html', context, context_instance=RequestContext(request))
		

# DRAFTSMEN -----------------------------------------------------------------
def DraftsmenAll(request):
	draftsmen = Draftsman.objects.all()
	context = {'draftsmen': draftsmen}
	return render_to_response('../templates/draftsmenall.html', context, context_instance=RequestContext(request))
	
def SpecificDraftsman(request, username):
	try:
		employee = Employee.objects.get(username=username)
		draftsman = Draftsman.objects.get(username=username)
		projects = Project.objects.filter(draftsman=draftsman.id)
		context = {'draftsman': draftsman, 'projects': projects}
	except:
		messages.error(request, 'That draftsman does not exist!')
		raise Http404("That draftsman does not exist!")
	return render_to_response('singledraftsman.html', context, context_instance=RequestContext(request))

# MACHINE TECHNICIANS ------------------------------------------------------------------
def MTsAll(request):
	mts = MachineTechnician.objects.all()
	context = {'mts': mts}
	return render_to_response('../templates/mtsall.html', context, context_instance=RequestContext(request))
	
def SpecificMT(request, username):
	try:
		employee = Employee.objects.get(username=username)
		mt = MachineTechnician.objects.get(username=username)
		projects = Project.objects.filter(machineTech=mt.id)
		context = {'mt': mt, 'projects': projects}
	except:
		messages.error(request, 'That Machine Technician does not exist!')
		raise Http404("That Machine Technician does not exist!")
	return render_to_response('singlemt.html', context, context_instance=RequestContext(request))
	
# MODEL BUILDERS ------------------------------------------------------------------
def MBsAll(request):
	mbs = ModelBuilder.objects.all()
	context = {'mbs': mbs}
	return render_to_response('../templates/mbsall.html', context, context_instance=RequestContext(request))
	
def SpecificMB(request, username):
	try:
		employee = Employee.objects.get(username=username)
		mb = ModelBuilder.objects.get(username=username)
		projects = Project.objects.filter(modelBuilder=mb.id)
		context = {'mb': mb, 'projects': projects}
	except:
		messages.error(request, 'That Model Builder does not exist!')
		raise Http404("That Model Builder does not exist!")
	return render_to_response('singlemb.html', context, context_instance=RequestContext(request))
	
	






	
	
	
