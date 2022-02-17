from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=20, default="")
    project_units = models.CharField(max_length=20, default="")
    project_area = models.CharField(max_length=20, default="")
    project_date = models.DateField(auto_now_add=True)
    project_time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.project_name


# class Units(models.Model):
#     project = models.ForeignKey(Project, on_delete = models.CASCADE)


