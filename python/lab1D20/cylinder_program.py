
from threedfigures import cylinder_volume, cylinder_surface_area, cylinder_curved_surface_area

radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))

csa = cylinder_curved_surface_area(radius, height)
tsa = cylinder_surface_area(radius, height)
vol = cylinder_volume(radius, height)

print(f"Curved Surface Area of Cylinder: {csa:.2f}")
print(f"Total Surface Area of Cylinder: {tsa:.2f}")
print(f"Volume of Cylinder: {vol:.2f}")