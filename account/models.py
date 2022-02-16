from django.db import models
import datetime

class Project(models.Model):
    project_name = models.CharField(max_length=20, default="")
    project_units = models.CharField(max_length=20, default="")
    project_area = models.CharField(max_length=20, default="")
    project_date = models.DateField(default = datetime.date.today)

    def __str__(self):
        return self.project_name

# class Units(models.Model):
#     project = models.ForeignKey(Project, on_delete = models.CASCADE)


