from .types import *

class Content():
    orientation = ORIENTATION[0]
    hardness = HARDNESS[1]
    duration = 600
    tags = []

    def __init__(self):
        pass

    def matching_rate(self, other):
        rate = 1
        if self.orientation != other.orientation:
            return 0

        if self.hardness != other.hardness:
            rate -= abs(HARDNESS.index(other.hardness) - HARDNESS.index(self.hardness)) / 10
        if self.duration != other.duration:
            bigger = self.duration if self.duration >= other.duration else other.duration
            smaller = other.duration if self.duration >= other.duration else self.duration
            rate -= abs((bigger - smaller) / bigger) / 2

        return rate