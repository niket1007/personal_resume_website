from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from portfolio.custom_field import MonthYearField
from datetime import date


class PersonalInformation(models.Model):
    '''
    Model will contain user information. It will have only one record
    '''
    
    name = models.CharField()
    profile = models.CharField()
    github_profile_link = models.URLField()
    linkedin_link = models.URLField()
    email = models.EmailField()
    short_description = models.CharField()


class Education(models.Model):
    '''
    Model will contain education related data
    '''

    institution_name  = models.CharField()
    degree = models.CharField()
    place = models.CharField()
    YEARS = [(i,i) for i in range(2013, date.today().year+1)]
    start_year = models.IntegerField(choices=YEARS)
    end_year = models.IntegerField(choices=YEARS, null=True, blank=True)

    def clean(self):
        super().clean()
        if self.end_year is not None and self.end_year < self.start_year:
            raise ValidationError({'end_date': 'End year cannot be earlier than start year.'})
    
    class Meta:
        ordering = ['-start_year', '-end_year']
    
class Experiences(models.Model):
    '''
    Model will contain experiences related data
    '''

    company_name = models.CharField()
    job_type = models.CharField(choices=[('intern', 'Intern'), ('full-time', 'Full-Time')])
    position = models.CharField()
    start_date = MonthYearField()
    end_date = MonthYearField(blank=True, null=True)
    description = models.CharField(
        help_text="Provide semicolon separated string and that will be converted to bullet points",
        blank=True)

    def clean(self):
        super().clean()
        if self.end_date is not None and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'End date cannot be earlier than start date.'})
    
    class Meta:
        ordering = ['-start_date', '-end_date']
    
    def __str__(self):
        return f'{self.company_name}-{self.job_type}'

class Skills(models.Model):
    '''
    Model will contain skills related data
    '''
    
    skill_name = models.CharField()
    skill_level = models.IntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5)])
    skill_devicon_class = models.CharField(help_text="Enter devicon class (https://devicon.dev/)")
    
    CATEGORY = [
        ('Programming Language', 'Programming Language'),
        ('Framework', 'Framework'),
        ('Database','Database'),
        ('Cloud', 'Cloud'),
        ('Tools', 'Tools')
    ]
    skill_category = models.CharField(choices=CATEGORY)

    class Meta:
        ordering = ['skill_category', '-skill_level'] 
    
    def __str__(self):
        return self.skill_name

class Projects(models.Model):
    '''
    Model will contain project related data
    '''
    
    proj_name = models.CharField(unique=True)
    proj_skills = models.ManyToManyField(Skills, blank=True)
    proj_desc = models.CharField(
        unique=True, 
        validators=[
            validators.MinLengthValidator(50),
        ])
    
    proj_code_link = models.URLField(
        unique=True,
        validators=[validators.URLValidator()]
        )

    proj_relates_to_exp = models.ForeignKey(Experiences, on_delete=models.SET_NULL, blank=True, null=True)

class Certifications(models.Model):
    '''
    Model will contain certification related data
    '''
    
    cert_name = models.CharField(unique=True)
    cert_start_date = MonthYearField()
    cert_end_date = MonthYearField(null=True, blank=True)
    cert_link = models.URLField(
        validators=[validators.URLValidator()],
        blank=True
        )

    def clean(self):
        super().clean()
        print(self.cert_start_date, self.cert_end_date)
        if self.cert_end_date is not None and self.cert_end_date < self.cert_start_date:
            raise ValidationError({'cert_end_date': 'End date cannot be earlier than start date.'})
    
    class Meta:
        ordering = ['-cert_end_date', '-cert_start_date']
