"""Package type based on dimensions and mass.

Determines whether a package is STANDARD, SPECIAL, or REJECTED based
on its volume and mass.
"""


REJECTED = "REJECTED"
SPECIAL = "SPECIAL"
STANDARD = "STANDARD"


class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass
        self.stack = self.get_stack()

    def is_bulky(self):
        return self.width * self.height * self.length >= 1000000 or self.width >= 150 or self.height >= 150 or self.length >= 150

    def is_heavy(self):
        return self.mass >= 20

    def get_stack(self):
        if self.is_bulky() and self.is_heavy():
            return REJECTED
        elif self.is_bulky() or self.is_heavy():
            return SPECIAL
        else:
            return STANDARD


def sort(width, height, length, mass):
    for name, value in (
        ("width", width),
        ("height", height),
        ("length", length),
        ("mass", mass),
    ):
        if value <= 0:
            raise ValueError(f"{name} must be positive")

    package = Package(width, height, length, mass)
    return package.stack