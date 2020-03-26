from .helpers import get_age_range

class User():
    age = 18
    sex = "male"
    mode = "discover"
    orientation_points = {
        "male": 0,
        "female": 1,
        "trans": 0
    }
    hardness_points = {
        "soft": 0.33933333334,
        "hard": 0.46666666666,
        "extreme": 0.194
    }
    type_points = {
        "blonde": 0.7114,
        "big-tits": 0.64,
        "teen": 0.443,
        "MILF": 0.387
    }

    def __init__(self):
        pass

    def matching_rate(self, other):
        rate = 1

        r1 = get_age_range(self.age)
        r2 = get_age_range(other.age)
        if r1 != r2:
            rate -= abs(r1 - r2) / 10
        
        if self.sex != other.sex:
            rate /= 1.3

        # TODO: mode
        # TODO: type

        # TODO: add other values like midian quartiles and ohters
        rate -= sum([
            abs(self.hardness_points['soft'] - other.hardness_points['soft']),
            abs(self.hardness_points['hard'] - other.hardness_points['hard']),
            abs(self.hardness_points['extreme'] - other.hardness_points['extreme'])
        ]) / 3

        rate -= sum([
            abs(self.orientation_points['male'] - other.orientation_points['male']),
            abs(self.orientation_points['female'] - other.orientation_points['female']),
            abs(self.orientation_points['trans'] - other.orientation_points['trans'])
        ]) / 3

        return rate
