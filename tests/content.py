from core.content import Content
from .helpers import is_in
from core.types import *

model = Content()
base = Content()

model.duration = 650
assert is_in(model.matching_rate(base), 0.95, 0.97), "Duration"
model.duration = 600

model.hardness = HARDNESS[0]
assert model.matching_rate(base) == 0.9, "Hardness 0"
model.hardness = HARDNESS[2]
assert model.matching_rate(base) == 0.9, "Hardness 2"
model.hardness = HARDNESS[3]
assert model.matching_rate(base) == 0.8, "Hardness 3"
model.hardness = HARDNESS[1]

model.orientation = "gay"
assert model.matching_rate(base) == 0, "Orientation"
model.orientation = "trans"
assert model.matching_rate(base) == 0, "Orientation"
model.orientation = "straight"

print("Content tests done!")