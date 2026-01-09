chai_order = dict(type = "Masala Chai", size = "Medium", sugar = 2)
print(chai_order)

chai_recipe = {}

chai_recipe["base"] = "black tea"
chai_recipe["liquids"] = ["water", "milk"]
print(f"Chai recipe so far: {chai_recipe}")

del chai_recipe["liquids"][1]
print(f"Chai recipe after deleting milk: {chai_recipe}")

chai_order = {
    "type": "Masala Chai",
    "size": "Medium",
    "sugar": 2
}

print(f" chai order details (Keys): {chai_order.keys()}")
print(f" chai order details (Values): {chai_order.values()}")
print(f" chai order details (Items): {chai_order.items()}")
chai_order.popitem()
print(f" chai order details after popitem: {chai_order.items()}")
extra_spices = {
    "cardamom": "crushed",
    "ginger": "sliced"
}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")   
chai_size = chai_order.get("size", "Regular")
print(f"Chai size from order: {chai_size}") 