from fractions import Fraction


# function for number str to float
def number_str_to_float(amount_str: str) -> (any, bool):
    # this function returns str amount to float and return it
    success = False
    number_as_float = amount_str
    
    try:
        number_as_float = float(sum(Fraction(s) for s in f"{amount_str}".split()))
    except:
        pass
    if isinstance(number_as_float, float):
        success = True
    return number_as_float, success