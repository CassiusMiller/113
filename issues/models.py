from django.db import models
from django.contrib.auth import get_user_model

class Status (models.Model):
  name = models.CharField (max_length=128)
  description = models.CharField (max_length=256)
  
  def __str__(self):
    return self.name
  
class Priority(models.Model):
  name = models.CharField (max_length=128)
  description = models.CharField (max_length=256)
  
  def __str__(self):
    return self.name

class Issue (models.Model):
  title = models.CharField (max_length=64)
  summary = models.CharField(max_length=128)
  description = models.CharField(null=True)
  status_id = models.ForeignKey(
    Status,
    on_delete = models.CASCADE
  )
  priority_id = models.ForeignKey(
    Priority,
    on_delete = models.CASCADE
  )
  reporter = models.ForeignKey(
    related_name="reporter",
    on_delete=models.CASCADE
  )