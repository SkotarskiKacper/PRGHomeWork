###
# Calculation of circle area and circumference 
#

# determine radius and PI values
Radius=float(input("Enter Circle radius: "))
Pi=355/113

# calculate area 
Area=Radius**2*Pi

# calculate circumference 
Circumference=Radius*2*Pi

# print results
print(f"""

circle area          : {round(Area,2)}
circle circumference : {round(Circumference,2)}
      
""")