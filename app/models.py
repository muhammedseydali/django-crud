from django.db import models

# Create your models here.
class table(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	contact_number = models.CharField(max_length=100)
	email = models.EmailField()
	profile_picture = models.FileField(upload_to='upload/images',null=True)

		