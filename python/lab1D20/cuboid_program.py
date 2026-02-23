from threedfigures import cuboid_volume, cuboid_surface_area, cuboid_curved_surface_area

length = float(input("Enter length of cuboid: "))
width = float(input("Enter width of cuboid: "))
height = float(input("Enter height of cuboid: "))

csa = cuboid_curved_surface_area(length, width, height)
tsa = cuboid_surface_area(length, width, height)
vol = cuboid_volume(length, width, height)

print(f"Curved Surface Area of Cuboid: {csa:.2f}")
print(f"Total Surface Area of Cuboid: {tsa:.2f}")
print(f"Volume of Cuboid: {vol:.2f}")