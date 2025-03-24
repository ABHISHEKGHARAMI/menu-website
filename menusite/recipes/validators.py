# this is the unit validators for checking later we update for third party package
from django.core.exceptions import ValidationError

valid_unit_measurements = ['kg','pound','ounce','oz','lbs']


def validate_unit_of_measurement(value):
    if value not in valid_unit_measurements:
        raise ValidationError(f'{value} is not a valid unit of measure..')
    


