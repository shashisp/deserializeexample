from django.db import models

class personal_info(models.Model):
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	contact_no = models.CharField(max_length=10)
	email = models.EmailField()
	profile_name=models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	pincode = models.CharField(max_length=10)
	#pid=models.IntegerField(primary_key=True, unique=True)
	pid = models.CharField(max_length=10)

class objective(models.Model):
	description = models.CharField(max_length=200)
	profile_name = models.CharField(max_length=100)
	#pid = models.ForeignKey('personal_info')
	pid = models.CharField(max_length=10)




class education(models.Model):
	degree_name = models.CharField(max_length=100)
	from_date = models.CharField(max_length=100)
	to_date = models.CharField(max_length=100)
	school_name = models.CharField(max_length=100)
	pid = models.CharField(max_length=10)


class skill(models.Model):
	skill_name = models.CharField(max_length=100)
	pid = models.CharField(max_length=10)

class achievement(models.Model):
	award_name = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	description = models.TextField(max_length=400)
	pid = models.CharField(max_length=10)

