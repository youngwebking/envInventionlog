from django.contrib import admin
from project.models import Project, Stl, Dxf

class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'number',)
	search_fields = ['name', 'number']
	
class StlAdmin(admin.ModelAdmin):
	list_display = ('stl',)
	search_fields = ['stl']
	
class DxfAdmin(admin.ModelAdmin):
	list_display = ('dxf',)
	search_fields = ['dxf']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Stl, StlAdmin)
admin.site.register(Dxf, DxfAdmin)
