from django.contrib import admin
from resume.models import personal_info, objective, education, skill, achievement


class personal_infoAdmin(admin.ModelAdmin):
	pass

class objectiveAdmin(admin.ModelAdmin):
	pass

class educationAdmin(admin.ModelAdmin):
	pass

class skillAdmin(admin.ModelAdmin):
	pass

class achievementAdmin(admin.ModelAdmin):
	pass

admin.site.register(personal_info, personal_infoAdmin)

admin.site.register(objective, objectiveAdmin)

admin.site.register(education, educationAdmin)

admin.site.register(skill, skillAdmin)

admin.site.register(achievement, achievementAdmin)