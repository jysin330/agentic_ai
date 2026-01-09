ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")

print(ingredients)

ingredients.remove("milk")
print(ingredients)

spice_options  = ["cardamom", "cloves", "cinnamon"]
chai_ingredients = ["milk", "water", "black tea"]
chai_ingredients.extend(spice_options)
print(chai_ingredients)
chai_ingredients.insert(0, "sugar")
print(chai_ingredients)
chai_ingredients.pop(5)
print(chai_ingredients)
chai_ingredients.sort()
print(chai_ingredients)
chai_ingredients.reverse()
print(chai_ingredients)

sugar_level = [1,2,3,4,5]
print(f"Highest sugar level: {max(sugar_level)}")
print(f"Lowest sugar level: {min(sugar_level)}")


base_liquids =["water", "milk"]
extra_flavours = ["vanilla", "caramel", "hazelnut"]
all_ingredients = base_liquids + extra_flavours
print(all_ingredients)

strong_brew = ["black tea" , "water"] * 3
print(strong_brew)

raw_spice_data = bytearray(b"cinnamon")
print(raw_spice_data)
raw_spice_data = raw_spice_data.replace(b"cinna", b"carda")
print(raw_spice_data.decode("utf-8"))