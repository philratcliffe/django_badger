import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_employee_name(value):
    """Only allow employee names that match this pattern"""
    if not re.match(r'^[A-Za-z\s\-\']+$', value):
        raise ValidationError('Invalid characerts in: {}'.format(value))
