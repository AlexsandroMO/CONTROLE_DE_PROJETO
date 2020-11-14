from django.contrib import admin
from . models import MyProject, Subject, DocumentStandard

class MyProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','comments')
    list_display = ('project_name','company','comments','created_proj','update_proj')
    

class DocumentStandardAdmin(admin.ModelAdmin):
    fields = ('documment_name', 'doc_type','doc_format','doc_type_page')
    list_display = ('documment_name', 'doc_type','doc_format','doc_type_page','created_sub','update_sub')


admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Subject)
admin.site.register(DocumentStandard, DocumentStandardAdmin)
