

class Ageerror(Exception):
    def __init__(self):
        print("Invalid age range")

class Heighterror(Exception):
    def __init__(self):
        print("Invalid Height range,enter in cm")


class weightterror(Exception):
    def __init__(self):
        print("Invalid weight range, enter in kg")