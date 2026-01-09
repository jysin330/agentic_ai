spice_mix = set()

print(f"Initial spice mix Id : {id(spice_mix)}")
spice_mix_id1 = id(spice_mix)

spice_mix.add("Ginger")
spice_mix.add("cinnemon")

print(f"Spice mix ID after adding elements: {id(spice_mix)}")

spice_mix_id2 = id(spice_mix)

print(spice_mix_id1 == spice_mix_id2)  # True, mutable object