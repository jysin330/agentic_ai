essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black paper"}
all_spices = essential_spices.union(optional_spices)
print(all_spices)

all_spices = essential_spices.intersection(optional_spices)
print(all_spices)
all_spices = essential_spices | optional_spices
print(all_spices)
all_spices = essential_spices & optional_spices
print(all_spices)

only_in_essential = essential_spices.difference(optional_spices)
print(only_in_essential)
only_in_essential = essential_spices - optional_spices
print(only_in_essential)

print(f"Is ginger an essential spice? {'ginger' in essential_spices}")

