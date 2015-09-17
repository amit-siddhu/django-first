from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	user = models.ForeignKey(User)
	task_name = models.CharField(max_length=140)
	task_detail = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.task_name