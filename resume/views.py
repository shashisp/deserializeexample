import json

from resume.models import personal_info, objective, education, skill, achievement 

from resume.serializers import personal_infoSerializer, objective_Serilaizer, education_Serializer, skill_Serializer, achievementSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response



def getjson(request):

	jsondata = request.DATA
	serializer = personal_infoSerializer(data= jsondata['personal_info'])
	if serializer.is_valid():
		serializer.save()
	else:
		raise serializers.ValidationError


	serializer = objectiveSerilaizer(data = jsondata['objective'])
	if serializer.is_valid():
		serializer.save()
	else:
		raise serializers.ValidationError

	serializer = education_Serializer(data = jsondata['education'])
	if serializer.is_valid():
		serializer.save()
	else:
		raise serializers.ValidationError

	serializer = skill_Serializer(data = jsondata['skill'])
	if serializer.is_valid():
		serializer.save()
	else:
		raise serializers.ValidationError

	serializer = achievementSerializer(data = jsondata['achievement'])
	if serializer.is_valid():
		serializer.save()
	else:
		 raise serializers.ValidationError

	return HttpResponseRedirect('/')



