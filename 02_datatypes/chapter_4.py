is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling
print(f"Total actions performed: {total_actions}") #upcasting boolean to integer

milk_present = 0 #no milk
print(f"Is milk present? {bool(milk_present)}") #downcasting integer to boolean


water_hot = True
tea_addded = False

can_serve_tea = water_hot and tea_addded
print(f"Can we server tea? {can_serve_tea}")
