# Data setup
fruits = ['apple', 'banana', 'cherry']
favorite = 'banana'
check = fruits

# Logical Operator: and
if favorite in fruits and len(fruits) > 2:
    print("Your favorite fruit is in the list and the list has more than 2 fruits.")

# Membership Operator: not in
if 'grape' not in fruits:
    print("Grape is not in the fruit list.")

# Identity Operator: is
if check is fruits:
    print("check and fruits refer to the same list object in memory.")

# Identity Operator: is not
if favorite is not None:
    print("Favorite fruit is not None.")
