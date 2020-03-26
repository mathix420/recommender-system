from .types import AGES

def get_age_range(age):
    for i, age_range in enumerate(AGES):
        if age in age_range:
            return i
    return None
