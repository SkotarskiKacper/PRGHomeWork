Price=float(input('enter product price: '))
Discount=float(input('enter product discount in percentage: '))

print(f"""

Product price       : {Price}
Product discount    : {Discount}% 
Price with discount : {round(Price-Price*Discount/100,2)}
Reduction           : {round(Price*Discount/100,2)}

""")
