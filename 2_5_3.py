###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a=float(input('a='))
c=float(input('b='))
b=float(input('c='))

Volume=a*b*c
SurfaceArea=2*a*b + 2*a*c + 2*b*c

print(f"""Cuboid with dimensions of {a} / {b} / {c}
Volume={Volume}
Surface Area={SurfaceArea}
""")