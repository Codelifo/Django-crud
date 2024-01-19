from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    id = models.IntegerField(primary_key = True)
    target_name = models.CharField( max_length=50)
    target_des = models.CharField( max_length=50)

