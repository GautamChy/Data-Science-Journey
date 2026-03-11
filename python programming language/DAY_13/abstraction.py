
# abstraction - concept of exposing only necessary details and hiding or irrelevant details from the user/outside world.

class Bike:
    brake = False
    acc = False
    clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Bike started")
        
obj1 = Bike()
obj1.start()