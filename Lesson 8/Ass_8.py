class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name):
        if app_name in self.app_list:
            print(f"{app_name} already installed")
        else:
            print(f"Installing {app_name}...")
            self.app_list.append(app_name)
            return self.app_list
    
    def delete_app(self, app_name):
        if app_name in self.app_list:
            print(f"Deleting {app_name}...")
            self.app_list.remove(app_name)
            return self.app_list
        else:
            print("App not installed")



device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()
device_a.install_app("Python")
device_a.install_app("Python")
print(device_a.app_list)
device_a.delete_app("Chrome")
device_a.delete_app("Python")
print(device_a.app_list)
