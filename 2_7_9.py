import random

Dice012=random.randint(1,6)

print(f"""
rolled dice    : {Dice012}
special number : {Dice012==1 or Dice012==6}
""")