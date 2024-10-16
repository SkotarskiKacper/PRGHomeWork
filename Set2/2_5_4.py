VatPercentage=23
Ammount=float(input('enter ammount:'))
print(f"""

Ammount : {Ammount}%
Vat     : {round(Ammount*VatPercentage/100,2)}%

""")
