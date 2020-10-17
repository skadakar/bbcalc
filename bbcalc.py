# This app is to figure out how much residual energy is in a projectile after a certain range given some basic parameters.
# Two versions will be available, one with more input variables and one basic for general usage.
# We do not account for the magnus effect for BBs with backspin nor do we account for humidity. 
# Real world results will always be lower than this, but this will give you the theoretical max.
#
# Remainder with all variables and remainder with commandline variables might be added.
#
# Assumed values is the default CQB legal limits for airsoft in norway. 
#energy_j = 0.9
#weight_g = 0.2
#weight_kg = weight_g/1000
#dragcoefficient = 0.47 # Assuming a circular projectile
#airdensity_kgm3 = 1.225 # 0 humidity at 0m above sealevel
#diameter_mm = 6 # 6mm 
#radius_m = diameter_mm / 1000 / 2
#crossection_m2 = math.pi*((radius_m)**2)
#distance_m = 30
#speed_ms = math.sqrt(energy_j/(0.5*weight_kg))

import math

def residual_simple(energy_j , weight_g , distance_m):
    if float(energy_j) * float(weight_g) * float(distance_m) == 0:
        print("Cannot have 0 as input value.")
    else:
        weight_kg = float(weight_g) / 1000
        dragcoefficient = float(0.47)
        airdensity_kgm3 = float(1.225)
        diameter_mm = int(6)
        radius_m = diameter_mm / 1000 / 2
        crossection_m2 = math.pi*((float(radius_m))**2)
        speed_ms = math.sqrt(float(energy_j)/(0.5*float(weight_kg)))
        step1 = airdensity_kgm3 * crossection_m2 * dragcoefficient
        step2 = 2 * weight_kg 
        speed_at_distance = speed_ms *math.exp(-((step1)/(step2)*int(distance_m)))
        energy_at_distance = 0.5 * weight_kg * speed_at_distance **2
        print(f"Energy at {distance_m}m is {energy_at_distance}")
        print(f"Speed at {distance_m}m is {speed_at_distance}")
        return speed_at_distance,energy_at_distance

# Get user inputs
energy = input("Energy at muzzle in joule ")
weight = input("Projectile weight in grams ")
distance = input("Distance in meters ")

# Send off the input to the function get_rema
get_residual = residual_simple(energy,weight,distance)

