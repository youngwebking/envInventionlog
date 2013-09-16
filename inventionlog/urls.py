from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventionlog.views.home', name='home'),
    # url(r'^inventionlog/', include('inventionlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
   (r'^static/(?P<path>.*)$', 'django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT}),
   (r'^$', 'static_pages.views.index'),
   (r'^terms/$', 'static_pages.views.terms'),
   (r'^help/$', 'static_pages.views.help'),
   (r'^employees/$', 'static_pages.views.EmployeesAll'),
   (r'^employees/upper-management/$', 'employee.views.ManagersAll'),
   (r'^employees/upper-management/(?P<username>.*)/$', 'employee.views.SpecificManager'),
   (r'^employees/production-managers/$', 'employee.views.PMsAll'),
	(r'^employees/production-managers/(?P<username>.*)/$', 'employee.views.SpecificPM'),
	(r'^employees/draftsmen/$', 'employee.views.DraftsmenAll'),
	(r'^employees/draftsmen/(?P<username>.*)/$', 'employee.views.SpecificDraftsman'),
	(r'^employees/machine-technicians/$', 'employee.views.MTsAll'),
	(r'^employees/machine-technicians/(?P<username>.*)/$', 'employee.views.SpecificMT'),
	(r'^employees/model-builders/$', 'employee.views.MBsAll'),
	(r'^employees/model-builders/(?P<username>.*)/$', 'employee.views.SpecificMB'),
	(r'^employees/set-status/(?P<username>.*)/$', 'employee.views.ChangeStatus'),
	(r'^projects/$', 'project.views.ProjectsAll'),
	(r'^projects/draft-upload/(?P<projectslug>.*)/$', 'project.views.upload_draft'),
	(r'^projects/model-upload/(?P<projectslug>.*)/$', 'project.views.upload_model'),
	(r'^projects/accept/(?P<projectslug>.*)/$', 'project.views.AcceptProject'),
	(r'^projects/approve-draft/(?P<projectslug>.*)/$', 'project.views.ApproveDraft'),
	(r'^projects/approve-prototype/(?P<projectslug>.*)/$', 'project.views.ApprovePrototype'),
	(r'^projects/approve-model/(?P<projectslug>.*)/$', 'project.views.ApproveModel'),
	(r'^projects/final-approve/(?P<projectslug>.*)/$', 'project.views.FinalApprove'),
	(r'^projects/(?P<projectslug>.*)/$', 'project.views.SpecificProject'),
	#(r'^add-project/$', 'project.views.AddProject'),
	(r'^register/$', 'employee.views.EmployeeRegistration'),
	(r'^login/(?P<username>.*)$', 'employee.views.Login'),
	(r'^logout/$', 'employee.views.LogoutRequest'),
	#(r'^profile/$', 'employee.views.Profile'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
