import math

Height=float(input('Enter Height: '))

Distance=3.57*math.sqrt(Height)
print("If you were to stand on the beach the horizon would be in ",Distance," kilometers")

Distance=3.57*math.sqrt(Height+20)
print("If you were to stand in the hotel window the horizon would be in ",Distance," kilometers")