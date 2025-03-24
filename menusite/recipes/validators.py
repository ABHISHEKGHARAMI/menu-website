# this is the unit validators for checking later we update for third party package
from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

valid_unit_measurements = ['kg','pound','ounce','oz','lbs']


def validate_unit_of_measurement(value):
    # registry to work with the pint
    ureg = pint.UnitRegistry()
    
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f'{value} is not a valid unit of measure..')
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f'{value} is not a valid unit of measure..')
    except ValidationError as e:
        raise ValidationError(f'{value} is not a valid unit of measure..')
    


