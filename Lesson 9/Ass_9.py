class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)
class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu
        
    def update_menu(self, new_coffee):
        self.coffee_menu.append(new_coffee)
        
    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu:
            print(f"Making {coffee_type}")
        else:
            print(f"{coffee_type} is not available. You can chose from this menu: ")
            print(my_coffee_machine.coffee_menu)
           
    
my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')

