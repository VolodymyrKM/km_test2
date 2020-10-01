class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.restaurant_name}.')
        print(f'The cuisine of the restaurant is {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name} is open!')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, set_number):
        self.number_served += set_number

# resto = Restaurant('Vizit', 'Ukraine')
#
# resto.set_number_served(5)
# resto.set_number_served(5)
#
# resto.increment_number_served(5)
# resto.increment_number_served(60)
#
# print(resto.number_served)
#
# #
# wite_rabbit = Restaurant('Rabbit', 'Traditional American')
#
# print(wite_rabbit.restaurant_name)
# print(wite_rabbit.cuisine_type)
#
# wite_rabbit.open_restaurant()
# wite_rabbit.describe_restaurant()


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def flavors_list(self):
        print(self.flavors)

ice_cream = IceCreamStand('Sweet Ice Cream', 'Sweety')

# ice_cream.flavors = ['chokolate', 'milk', 'banana']

ice_cream.flavors_list()


