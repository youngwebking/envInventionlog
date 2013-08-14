from django.contrib import admin
from employee.models import Employee, Manager, ProductionManager, Draftsman, MachineTechnician, ModelBuilder

class EmployeeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'job',)
	search_fields = ['name', 'job']

class ManagerAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name']

class PMAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug': ('name',)}
	list_display = ('name',)
	search_fields = ['name']
	
class DraftsmenAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug': ('name',)}
	list_display = ('name',)
	search_fields = ['name']
	
class MachineTechAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug': ('name',)}
	list_display = ('name',)
	search_fields = ['name']
	
class MBAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug': ('name',)}
	list_display = ('name',)
	search_fields = ['name']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(ProductionManager, PMAdmin)
admin.site.register(Draftsman, DraftsmenAdmin)
admin.site.register(MachineTechnician, MachineTechAdmin)
admin.site.register(ModelBuilder, MBAdmin)
