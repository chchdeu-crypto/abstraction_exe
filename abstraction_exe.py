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

#mission 3
class DeliveryMethod(ABC):
    def __init__(self,compeny_name):
        self.compeny_name=compeny_name
    @abstractmethod
    def deliver(self,order_id):
        pass
class Bikedelivery(DeliveryMethod):
    def __init__(self,compeny_name):
        super().__init__(compeny_name)
    def deliver(self, order_id):
        print(f"[{self.compeny_name}] order {order_id} - bike delivery")
class Dronedelivery(DeliveryMethod):
    def __init__(self,compeny_name):
        super().__init__(compeny_name)
    def deliver(self, order_id):
        print(f"[{self.compeny_name}] order {order_id} - bike drone")
bike=Bikedelivery("fedex")
bike.deliver(303)
drone=Dronedelivery("amazon")
drone.deliver(303)

#mission 4
class DeliveryMethod(ABC):
    @abstractmethod
    def delivery(self,order_id):
        pass
    @abstractmethod
    def get_data(self):
        pass
class Bikedelivery(DeliveryMethod):
    def delivery(self, order_id):
        print(f"order {order_id} deliverd by bike")
    def get_data(self):
        return 30
class Dronedelivery(DeliveryMethod):
    def delivery(self, order_id):
        print(f"order {order_id} brought to your building by drone")
    def get_data(self):
        return 15
bike=Bikedelivery()
bike.delivery(1)
print(bike.get_data())
drone=Dronedelivery()
drone.delivery(1)
print(drone.get_data())

#mission 5
class DeliveryMethod(ABC):
    @abstractmethod
    def delivery(self,order_id):
        pass
class Brokendelivery(DeliveryMethod):
    def delivery(self, order_id):
        print(f"order {order_id} orderd seccsefuly ")
broken=Brokendelivery()
broken.delivery(2)

#mission 6
class Deliveryfee:
    @staticmethod
    def calc(distance_km,rate_per_km):
        return distance_km*rate_per_km
    @staticmethod
    def with_surcherge(base_fee,surcharge_percent):
        return base_fee*(1+surcharge_percent/100)
    @staticmethod
    def is_free(distance_km):
        return True if distance_km<=2.0 else False
print(Deliveryfee.calc(5,3.0))
print(Deliveryfee.with_surcherge(15.0,10))
print(Deliveryfee.is_free(1.5))

        
