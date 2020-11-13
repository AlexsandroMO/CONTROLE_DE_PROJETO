from django.contrib import admin

from . models import MyProject, Subject, DocumentStandard

admin.site.register(MyProject)
admin.site.register(Subject)
admin.site.register(DocumentStandard)
