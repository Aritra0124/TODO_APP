from django.db import models

class TodoTask(models.Model):
    task_gid = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    task_note = models.CharField(max_length=100, null=True, blank=True)
    task_section = models.CharField(max_length=100)
    task_section_gid = models.CharField(max_length=100)

