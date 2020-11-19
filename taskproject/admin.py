from django.contrib import admin
from . models import MyProject, Subject, DocumentStandard, Action, StatusDoc, Employee, Cotation, Upload

class MyProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','comments')
    list_display = ('project_name','company','comments','created_proj','update_proj')
    

class DocumentStandardAdmin(admin.ModelAdmin):
    fields = ('documment_name', 'doc_type','doc_format','doc_type_page')
    list_display = ('documment_name', 'doc_type','doc_format','doc_type_page','created_doc','update_doc')


class SubjectAdmin(admin.ModelAdmin):
    fields = ('subject_name',)
    list_display = ('subject_name', 'created_sub','update_sub')


class CotationAdmin(admin.ModelAdmin):
    fields = ('proj_name', 'subject_name', 'doc_name', 'qt_page', 'qt_doc', 'qt_hh','cost_hh','cost_doc')
    list_display = ('proj_name', 'subject_name', 'doc_name', 'qt_page', 'qt_doc', 'qt_hh','cost_hh','cost_doc','created_ct','update_ct')
     
 
class UploadAdmin(admin.ModelAdmin):
    fields = ('arq',)
    list_display = ('arq', 'update_arq')

admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(DocumentStandard, DocumentStandardAdmin)
admin.site.register(Action)
admin.site.register(StatusDoc)
admin.site.register(Employee)
admin.site.register(Cotation)
admin.site.register(Upload)
