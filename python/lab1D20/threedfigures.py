# threedfigures.py

import math

# ---------------- Cube ----------------
def cube_volume(side):
    return side ** 3

def cube_surface_area(side):
    return 6 * side ** 2

def cube_curved_surface_area(side):
    # For a cube, CSA = 4 * side^2
    return 4 * side ** 2

# ---------------- Cuboid ----------------
def cuboid_volume(length, width, height):
    return length * width * height

def cuboid_surface_area(length, width, height):
    return 2 * (length*width + width*height + length*height)

def cuboid_curved_surface_area(length, width, height):
    # CSA = 2 * height * (length + width)
    return 2 * height * (length + width)

# ---------------- Cylinder ----------------
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_curved_surface_area(radius, height):
    return 2 * math.pi * radius * height

# ---------------- Cone ----------------
def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

def cone_surface_area(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def cone_curved_surface_area(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * slant_height

# ---------------- Sphere ----------------
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

def sphere_curved_surface_area(radius):
    # For sphere, CSA = TSA
    return 4 * math.pi * radius ** 2

# ---------------- Hemisphere ----------------
def hemisphere_volume(radius):
    return (2/3) * math.pi * radius ** 3

def hemisphere_surface_area(radius):
    return 3 * math.pi * radius ** 2

def hemisphere_curved_surface_area(radius):
    return 2 * math.pi * radius ** 2