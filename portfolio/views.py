from django.shortcuts import render
from django.views.generic.base import TemplateView
from portfolio import models

class MainView(TemplateView):
    template_name = 'portfolio/index.html'

    @staticmethod
    def transform_skills(skills_list):
        transformed_skills_list = []
        for category in models.Skills.CATEGORY:
            transformed_skills_list.append([category[0], []])
        
        for skill in skills_list:
            category = skill.skill_category
            cat_index = models.Skills.CATEGORY.index((category, category))
            transformed_skills_list[cat_index][1].append(skill)
        return transformed_skills_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences_list"] = models.Experiences.objects.all()
        context["skills_list"] = MainView.transform_skills(models.Skills.objects.all())
        context["project_list"] = models.Projects.objects.all()
        context["education_list"] = models.Education.objects.all()
        context["certification_list"] = models.Certifications.objects.all()
        context["personal_info"] = models.PersonalInformation.objects.all()[0]
        return context
