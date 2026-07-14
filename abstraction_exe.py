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