# Author: GTX - MB 2024
# Problem description : Calculate a path width around a fountain
# Last modification on : September, 10, 2024
# Known problems/bugs :

# IMPORTATIONS
from math import pi, sqrt
from typing import Final

# CONSTANTS
FOUNTAIN_RADIUS: Final = 1
IDEAL_PATH_WIDTH: Final = 2

# VARIABLES
asphalt_in_truck: float  # Asking the user, in cubic meters.
fountain_area: float  # Next 4 values will be calculated later
total_area: float
path_width: float
asphalt_needed: float


# LOGIC
fountain_area = pi * FOUNTAIN_RADIUS ** 2
asphalt_needed = round(pi * (IDEAL_PATH_WIDTH + FOUNTAIN_RADIUS) ** 2 - fountain_area, 2)

asphalt_in_truck = float(input("Enter the amount of asphalt left in the truck (in cubic meters): "))
total_area = fountain_area + asphalt_in_truck

path_width = round(sqrt(total_area / pi) - FOUNTAIN_RADIUS, 2)

if asphalt_in_truck >= asphalt_needed:
    print(f"Path width : {path_width} METERS \n\n - For an ideal path of 2 meters - \nAsphalt needed for the path: "
          f"{asphalt_needed} CUBIC METERS\nAsphalt left: {round(asphalt_in_truck - asphalt_needed, 2)} CUBIC METERS")
    quit()

print(f"Path width : {path_width} METERS \n\n - For an ideal path of 2 meters - \nAsphalt needed for the path: "
      f"{asphalt_needed} CUBIC METERS\nAsphalt to add: {round(asphalt_needed - asphalt_in_truck, 2)} CUBIC METERS")