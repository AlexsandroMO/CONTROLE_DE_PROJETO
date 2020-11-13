from django.db import models


class MyProject(models.Model):


    project_name = models.CharField(max_length=255)
    company = models.TextField()
    comments = models.TextField()
    created_proj = models.DateTimeField(auto_now_add=True)
    update_proj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Subject(models.Model):

    subject_name = models.CharField(max_length=255)
    created_sub = models.DateTimeField(auto_now_add=True)
    update_sub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


class DocumentStandard(models.Model):

    documment_name = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=3)
    doc_format = models.CharField(max_length=15)
    doc_type_page = models.CharField(max_length=2)
    created_sub = models.DateTimeField(auto_now_add=True)
    update_sub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doc_type


