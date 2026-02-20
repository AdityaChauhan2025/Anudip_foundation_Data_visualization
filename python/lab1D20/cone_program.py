
from threedfigures import cone_volume, cone_surface_area, cone_curved_surface_area

radius = float(input("Enter radius of cone: "))
height = float(input("Enter height of cone: "))

csa = cone_curved_surface_area(radius, height)
tsa = cone_surface_area(radius, height)
vol = cone_volume(radius, height)

print(f"Curved Surface Area of Cone: {csa:.2f}")
print(f"Total Surface Area of Cone: {tsa:.2f}")
print(f"Volume of Cone: {vol:.2f}")