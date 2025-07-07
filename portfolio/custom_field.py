from datetime import date
from django import forms
from django.db import models

class CustomDateInput(forms.DateInput):

    def __init__(self, attrs=None):
        default_attrs = {
            'type': 'month',
            'class': 'form-control',
            'placeholder': 'YYYY-MM or YYYY-MM-DD'
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
    
    def format_value(self, value):
        """Format the value for display in the widget"""
        if value is None:
            return ''
        if isinstance(value, date):
            if value.day:
                return value.strftime('%Y-%m-%d')
            else:
                return value.strftime('%Y-%m')
        return str(value)


class MonthYearFormField(forms.DateField):
    """Custom form field for month/year input"""
    
    widget = CustomDateInput
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('input_formats', ['%Y-%m', '%Y-%m-%d'])
        super().__init__(*args, **kwargs)
    
    def clean(self, value):
        """Clean and validate the input"""
        value = super().clean(value)
        if value:
            # Always set day to 1 for consistency
            if not value.day:
                return date(value.year, value.month, 1)
        return value

class MonthYearField(models.DateField):
    """
    Custom model field having default day as 1
    """
    
    description = "Month and Year field stored as date"
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('help_text', 'Selection as YEAR-MONTH or YEAR-MONTH-DAY')
        super().__init__(*args, **kwargs)
    
    def clean(self, value, model_instance):
        """Clean the value before saving to database"""
        if value is None:
            return value
        
        if isinstance(value, date):
            # Always set day to 1
            if not value.day:
                value = date(value.year, value.month, 1)
        
        return super().clean(value, model_instance)
    
    def to_python(self, value):
        """Convert database value to Python object"""
        if value is None:
            return value
        
        if isinstance(value, date):
            return value
        
        return super().to_python(value)
    
    def get_prep_value(self, value):
        """Convert Python object to database value"""
        if value is None:
            return value
        
        if isinstance(value, date):
            # Always store as first day of month
            if not value.day:
                value = date(value.year, value.month, 1)
        
        return super().get_prep_value(value)
    
    def formfield(self, **kwargs):
        """Return form field for this model field"""
        defaults = {
            'form_class': MonthYearFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)