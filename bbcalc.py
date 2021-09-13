# This app is to figure out how much residual energy is in a projectile after a certain range given some basic parameters.
# Two versions will be available, one with more input variables and one basic for general usage.
# We do not account for the magnus effect for BBs with backspin nor do we account for humidity.
# Real world results will always be lower than this, but this will give you the theoretical max.
#
# Remainder with all variables and remainder with commandline variables might be added.
#
# Assumed values is the default CQB legal limits for airsoft in norway.
# energy_j = 0.9
# weight_g = 0.2
# weight_kg = weight_g/1000
# dragcoefficient = 0.47 # Assuming a circular projectile
# airdensity_kgm3 = 1.225 # 0 humidity at 0m above sealevel
# diameter_mm = 6 # 6mm
# radius_m = diameter_mm / 1000 / 2
# crossection_m2 = math.pi*((radius_m)**2)
# distance_m = 30
# speed_ms = math.sqrt(energy_j/(0.5*weight_kg))

#from flask import Flask
import math


def residual_simple(energy_j: float, weight_g: float, distance_m: float):
    if energy_j * weight_g * distance_m == 0:
        raise ValueError("Cannot have 0 as input value.")

    # Constants
    weight_kg = weight_g / 1000
    dragcoefficient = 0.47
    airdensity_kgm3 = 1.225
    diameter_mm = 6

    radius_m = diameter_mm / 1000 / 2
    crossection_m2 = math.pi * (radius_m ** 2)
    speed_ms = math.sqrt(energy_j / (0.5 * weight_kg))
    drag_ish = airdensity_kgm3 * crossection_m2 * dragcoefficient
    speed_at_distance = speed_ms * math.exp(-(drag_ish / (weight_kg * 2) * distance_m))
    energy_at_distance = 0.5 * weight_kg * speed_at_distance ** 2
    return speed_at_distance, energy_at_distance


# Request input and print result only if it's run as a script.
if __name__ == "__main__":
    # Get user inputs
    energy = float(input("Energy at muzzle in joule "))
    weight = float(input("Projectile weight in grams "))
    distance = float(input("Distance in meters "))

    speed_at_distance, energy_at_distance = residual_simple(energy, weight, distance)

    print(f"Energy at {distance}m is {energy_at_distance}J")
    print(f"Speed at {distance}m is {speed_at_distance} m/s")
