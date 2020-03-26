from .helpers import is_in
from core.user import User
from core.types import *

model = User()
base = User()

model.age = 22
assert model.matching_rate(base) == 1, "Age"
model.age = 25
assert model.matching_rate(base) == 0.9, "Age"
model.age = 35
assert model.matching_rate(base) == 0.8, "Age"
model.age = 45
assert model.matching_rate(base) == 0.7, "Age"
model.age = 55
assert model.matching_rate(base) == 0.6, "Age"
model.age = 100
assert model.matching_rate(base) == 0.5, "Age"
model.age = base.age

model.hardness_points = {
    "extreme": 0.33933333334,
    "soft": 0.46666666666,
    "hard": 0.194
}
assert is_in(model.matching_rate(base), 0.78, 0.82), "Hardness"


model.hardness_points = {
    "hard": 0.05,
    "extreme": 0.9,
    "soft": 0.05
}
assert is_in(model.matching_rate(base), 0.52, 0.55), "Hardness"
model.hardness_points = base.hardness_points.copy()


model.orientation_points = {
    "male": 1,
    "female": 0,
    "trans": 0
}
assert is_in(model.matching_rate(base), 0.33, 0.34), "Hardness"

model.orientation_points = {
    "male": 0.5,
    "female": 0.5,
    "trans": 0
}
assert is_in(model.matching_rate(base), 0.66, 0.67), "Hardness"
model.hardness_points = base.hardness_points.copy()

print("User tests done!")