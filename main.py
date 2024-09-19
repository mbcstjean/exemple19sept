# Author: GTX - MB 2024
# Problem description : Calculate a path width around a fountain
# Last modification on : September, 12, 2024
# Known problems/bugs : 1- If user enter a string in the asphalt_in_truck variable, program won't work
# IMPORTATIONS
from math import pi, sqrt
from typing import Final

# CONSTANTS
FOUNTAIN_RADIUS: Final = 1
IDEAL_PATH_WIDTH: Final = 2

# VARIABLES
asphalt_in_truck: float  # Asking the user, in square meters.
fountain_area: float  # Next 4 values will be calculated later
total_area: float
path_width: float
asphalt_needed: float


# CODE LOGIC
fountain_area = pi * FOUNTAIN_RADIUS ** 2  # Fountain area in square meters
# Asphalt needed to build a path of 2 meters of width
asphalt_needed = round(pi * (IDEAL_PATH_WIDTH + FOUNTAIN_RADIUS) ** 2 - fountain_area, 2)
# Ask the user to enter the amount of asphalt left in the truck
asphalt_in_truck = float(input("Enter the amount of asphalt left in the truck (in square meters): "))
total_area = fountain_area + asphalt_in_truck  # Area of the fountain + the path around it

path_width = round(sqrt(total_area / pi) - FOUNTAIN_RADIUS, 2)  # Path width of the buildable path with the asphalt left

if asphalt_in_truck >= asphalt_needed:  # Check if we have more asphalt than required
    print(f"\nPath width with this amount of asphalt in the truck: {path_width} METERS \n\n "
          f"- For an ideal path of 2 meters - \nAsphalt needed for the ideal path: {asphalt_needed} SQUARE METERS\n"
          f"Asphalt left after path construction: {round(asphalt_in_truck - asphalt_needed, 2)} SQUARE METERS")
    quit()
# Quit the program after printing the results because we have more asphalt than needed, so we don't print
# the next statement, which is for if we have less asphalt than required
print(f"\nPath width with this amount of asphalt in the truck: {path_width} METERS \n\n - For an ideal path of 2 meters"
      f"- \nAsphalt needed for the ideal path: {asphalt_needed} SQUARE METERS\nAsphalt to add for path construction: "
      f"{round(asphalt_needed - asphalt_in_truck, 2)} SQUARE METERS")
