from abc import ABC,abstractmethod

#mission 1
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class Bikedelivery(DeliveryMethod):
    def __init__(self):
        super().__init__()
    def deliver(self, order_id):
        print(f"order {order_id} deliverd by bike")
bike=Bikedelivery()
bike.deliver(101)

#mission 2
class DeliveryMethod(ABC):
    @abstractmethod
    def delivery(self,order_id):
        pass
class Dronedelivery(DeliveryMethod):
    def __init__(self):
        super().__init__()
    def delivery(self,order_id):
        print(f"order {order_id} brought to your building by drone")
class Cardelivery(DeliveryMethod):
    def __init__(self):
        super().__init__()
    def delivery(self,order_id):
        print(f"order {order_id} brought to your building by car")
drone=Dronedelivery()
drone.delivery(202)
car=Cardelivery()
car.delivery(202)