from django.contrib import admin
from portfolio import models

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['proj_name', 'get_proj_skills', 
                    'proj_desc', 'proj_code_link', 'proj_relates_to_exp']
    search_fields = ['proj_name']
    list_filter = ['proj_name']

    def get_proj_skills(self, obj):
        return ", ".join([skill.skill_name for skill in obj.proj_skills.all()])
    
    get_proj_skills.short_description = 'proj_skills'
admin.site.register(models.Projects, ProjectModelAdmin)

class CertificationsModelAdmin(admin.ModelAdmin):
    list_display = ['cert_name', 'cert_start_date', 'cert_end_date', 'cert_link']
    search_fields = ['cert_name']
    list_filter = ['cert_name']
admin.site.register(models.Certifications, CertificationsModelAdmin)

class EducationModelAdmin(admin.ModelAdmin):
    list_display = ['institution_name', 'degree', 'place', 'start_year', 'end_year']
    search_fields = ['institution_name']
    list_filter = ['institution_name']
admin.site.register(models.Education, EducationModelAdmin)

class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_type', 'position', 'start_date', 'end_date', 'description']
    search_fields = ['company_name']
    list_filter = ['company_name']
admin.site.register(models.Experiences, ExperienceModelAdmin)

class SkillModelAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'skill_level', 'skill_category','skill_devicon_class']
    search_fields = ['skill_name']
    list_filter = ['skill_level', 'skill_category']
admin.site.register(models.Skills, SkillModelAdmin)


class PersonalInfoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description', 'profile','github_profile_link', 'linkedin_link', 'email']
admin.site.register(models.PersonalInformation, PersonalInfoModelAdmin)