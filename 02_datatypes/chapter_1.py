sugar_amount = 2
print(f"Initial sugar amount: {sugar_amount} teaspoons")

print(f" Id of sugar_amount variable: {id(sugar_amount)}")

sugar_amount = 22 # immutable (only the reference is changing)
print(f" Second Initial sugar amount: {sugar_amount} teaspoons")

print(f" Id of sugar_amount variable: {id(sugar_amount)}")