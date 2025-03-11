from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError


valid_unit_measurements =  ['pound','lbs','oz','gram']


def validate_unit_measure(value):
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"{value} does not support the unit.")
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value.lower()]
    except UndefinedUnitError as e:
        raise ValidationError(e)
    except:
        raise ValidationError(f"{value} does not support the unit.")
