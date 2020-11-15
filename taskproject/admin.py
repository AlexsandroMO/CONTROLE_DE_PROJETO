from django.contrib import admin
from . models import MyProject, Subject, DocumentStandard, Action, StatusDoc, Employee

class MyProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','comments')
    list_display = ('project_name','company','comments','created_proj','update_proj')
    

class DocumentStandardAdmin(admin.ModelAdmin):
    fields = ('documment_name', 'doc_type','doc_format','doc_type_page')
    list_display = ('documment_name', 'doc_type','doc_format','doc_type_page','created_doc','update_doc')


class SubjectAdmin(admin.ModelAdmin):
    fields = ('subject_name',)
    list_display = ('subject_name', 'created_sub','update_sub')


admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(DocumentStandard, DocumentStandardAdmin)
admin.site.register(Action)
admin.site.register(StatusDoc)
admin.site.register(Employee)
