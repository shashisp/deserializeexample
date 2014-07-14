from resume.models import personal_info, objective, education, skill, achievement
from rest_framework import serializers


class personal_infoSerializer(serializers.Serializer):
	address = serializers.CharField(max_length=200)
	city = serializers.CharField(max_length=100)
	contact_no = serializers.CharField(max_length=10)
	email = serializers.CharField(max_length=100)
	profile_name = serializers.CharField(max_length=100)
	pincode = serializers.CharField(max_length=100)
	pid = serializers.IntegerField()


	def restore_object(self, attrs, instance=None):

		if instance:

			instance.address = attrs.get('address', instance.address)
			instance.city = attrs.get('city', instance.city)
			instance.contact_no = attrs.get('contact_no', instance.contact_no)
			instance.email = attrs.get('email', instance.email)
			instance.profile_name = attrs.get('profile_name', instance.profile_name)
			instance.pincode = attrs.get('pincode', instance.pincode)
			instance.pid =attrs.get('pid', instance.pid)
			return instance

		return personal_info(**attrs)


class objective_Serilaizer(serializers.Serializer):
	description = serializers.CharField(max_length=200)
	profile_name = serializers.CharField(max_length=100)
	pid = serializers.IntegerField()

	def restore_object(self, attrs, instance=None):

		if instance:
			instance.description = attrs.get('description', instance.description)
			instance.profile_name = attrs.get('profile_name', instance.profile_name)
			instance.pid = attrs.get('pid', instance.pid)
			return instance
		return objective(**attrs)

class education_Serializer(serializers.Serializer):
	degree_name = serializers.CharField(max_length=200)
	from_date = serializers.CharField(max_length=200)
	to_date = serializers.CharField(max_length=200)
	school_name = serializers.CharField(max_length=200)

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.degree_name = attrs.get('degree_name', instance.degree_name)
			instance.from_date = attrs.get('from_date', instance.from_date)
			instance.to_date = attrs.get('to_date', instance.to_date)
			instance.school_name = attrs.get('school_name', instance.school_name)
			return instance
		return education(**attrs)

class skill_Serializer(serializers.Serializer):
	skill_name = serializers.CharField(max_length=100)
	pid = serializers.CharField(max_length=100)

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.skill_name = attrs.get('skill_name', instance.skill_name)
			instance.pid = attrs.get('pid', instance.pid)
			return instance
		return skill(**attrs)

class achievementSerializer(serializers.Serializer):
	award_name = serializers.CharField(max_length=100)
	date = serializers.CharField(max_length=100)
	description = serializers.CharField(max_length=100)

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.award_name = attrs.get('award_name', instance.award_name)
			instance.date = attrs.get('date', instance.date)
			instance.description = attrs.get('description', instance.description)
			return instance
		return achievement(**attrs)

 

