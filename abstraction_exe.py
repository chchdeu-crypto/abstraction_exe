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
        print(f"[{self.compeny_name}] order {order_id} - by drone")
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

#mission 7
class DeliveryMethod(ABC):
    @abstractmethod
    def delivery(self,order_id):
        pass
    @abstractmethod
    def get_ate(self):
        pass
class Walkingdelivery(DeliveryMethod):
    def delivery(self, order_id):
        return
    def get_ate(self):
        return 60
class Expresdelivery(DeliveryMethod):
    def delivery(self, order_id):
        return 
    def get_ate(self):
        return 10
class Deliveryhelper:
    @staticmethod
    def faster(d1,d2):
        if d1.get_ate()>d2.get_ate():
            return d2
        else:
            return d1
walk=Walkingdelivery()
experas=Expresdelivery()
faster=Deliveryhelper.faster(walk,experas)
print(f"faster option: {faster.__class__.__name__}")

#mission 8
class Notifier(ABC):
    @abstractmethod
    def send(self,recipinet,message):
        pass
class Pushnotifier(Notifier):
    def send(self, recipinet, message):
        print(f"push to {recipinet}: {message}")
class Whatapp(Notifier):
    def send(self, recipinet, message):
        print(f"whatsapp to {recipinet}: {message}")
class Inappnotifier(Notifier):
    def send(self, recipinet, message):
        print(f"in app banner for {recipinet}: {message}")
messages=[Pushnotifier(),Whatapp(),Inappnotifier()]
for message in messages:
    message.send("customer 42","your order is on the way")

#mission 9
class Restaurant(ABC):
    @abstractmethod
    def get_menu(self):
        pass
    @abstractmethod
    def prepare_order(self,item_menu):
        pass
class ItalianRestaurant(Restaurant):
    def get_menu(self):
        return ["pasta","pizza","tiramisu"]
    def prepare_order(self, item_menu):
        print(f"bon appetito! your {item_menu} ")
class Sushirestaurant(Restaurant):
    def get_menu(self):
        return ["maki","nigiri","ramen"]
    def prepare_order(self, item_menu):
        print(f"enjoy your japanis {item_menu}")
class Burgerjoint(Restaurant):
    def get_menu(self):
        return ["burger","frice","shake"]
    def prepare_order(self, item_menu):
        print(f"grilling your {item_menu}")
resturants=[ItalianRestaurant(),Sushirestaurant(),Burgerjoint()]
for r in resturants:
    print(f"{r.get_menu()}")
    r.prepare_order("burger")

#mission 10
class Deliverymethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass 
    def get_eta(self):
        pass
    def get_cost(self,distance_km):
        pass
class Bikedelivery(Deliverymethod):
    def deliver(self, order_id):
        return f"order {order_id} dliverd by bike"
    def get_eta(self):
        return 30
    def get_cost(self, distance_km):
        return 3*distance_km
class dronedelivery(Deliverymethod):
    def deliver(self, order_id):
        return f"order {order_id} dliverd by drone"
    def get_eta(self):
        return 10
    def get_cost(self, distance_km):
        return 12*distance_km
class cardelivery(Deliverymethod):    
    def deliver(self, order_id):
        return f"order {order_id} dliverd by car"
    def get_eta(self):
        return 20
    def get_cost(self, distance_km):
        return 10*distance_km
class walkingdelivery(Deliverymethod):
    def deliver(self, order_id):
        return f"order {order_id} dliverd by walk"
    def get_eta(self):
        return 45
    def get_cost(self, distance_km):
        return 2*distance_km
# class platform:
#     def __init__(self):
#         self.optional_del=[Bikedelivery(),dronedelivery(),cardelivery(),walkingdelivery()]
#     def cheapest_option(self,distance_km):
#         lowes_cost=self.optional_del[0].get_cost(distance_km)
#         for o in self.optional_del:
#             if o.get_cost(distance_km)<lowes_cost:
#                 lowes_cost=o.get_cost
#         return lowes_cost
#     def fastest_option(self):
#         lowest_time=self.optional_del[0].get_eta()
#         for l in self.optional_del:
#             if l.get_eta() <lowest_time:
#                 lowest_time=l.get_eta
#         return lowest_time




# a1=platform()
# print(a1.cheapest_option(5))
# print(a1.fastest_option())


class Platform:
    def __init__(self):
        self.optional_del=[Bikedelivery(),dronedelivery(),cardelivery(),walkingdelivery()]
    def cheapest_option(self, distance_km):
        cheapest = self.optional_del[0]
        lowest_cost = cheapest.get_cost(distance_km)
        for d in self.optional_del:
            if d.get_cost(distance_km) < lowest_cost:
                cheapest = d
                lowest_cost = d.get_cost(distance_km)
        return cheapest
    def fastest_option(self):
        fastest = self.optional_del[0]
        lowest_time = fastest.get_eta()
        for d in self.optional_del:
            if d.get_eta() < lowest_time:
                fastest = d
                lowest_time = d.get_eta()
        return fastest
platform = Platform()
print(f"cheapast: {platform.cheapest_option(5).__class__.__name__}")
print(f"fastest: {platform.fastest_option().__class__.__name__}")