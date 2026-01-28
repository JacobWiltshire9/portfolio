# Create a class for the business
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Create a class for the franchise
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  # Create a string rep to say which location you're at
  def __repr__(self):
    return f"Current Franchise Location: {self.address}\n"
  
  # Create a method to tell customers the available menus
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# Create class for Menu
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  # String Rep. a sentence for the times when the menus are available
  def __repr__(self):
    return f"{self.name} menu will be available from  {self.start_time} - {self.end_time}"

  # Create a method to calculate the bill
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return f"The bill for ordering {purchased_items} will come out to ${bill:.2f}\n" 

# Brunch Menu
brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch, 1100, 1600)

# Early Bird Menu
early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird, 1500, 1800)

# Dinner Menu
dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner, 1700, 2300)

# Kids Menu
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids Menu', kids, 1100, 2100)

# Test the calculate bill method
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Store all menus into one list
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Store address and menus in locations
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)
print(flagship_store.available_menus(1700))

# Create a list with both franchises in it
basta_franchises = [flagship_store, new_installment]

# Create first business
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Create menu for Take a' Arepa
arepas ={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas, 1000, 2000)

# Store address locations for Aerpas
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Create second Business
arepas = Business("Take a' Arepa", [arepas_place])


print(arepas.franchises[0].menus[0])

# AI Review - The code implements the core classes (Menu, Franchise, Business) and wires them together to model a multi-restaurant system as described in the project tasks.
# The class and method names are descriptive and reflect their roles (Menu, Franchise, Business).
# The available_menus method efficiently filters menus by time in a single pass.