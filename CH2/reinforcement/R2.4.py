#class named Flower that has three getters and setters, one to set and return the flowers name, next to set and return the num of petals, and lastly to set and return the price

class Flower():
    def __init__(self, name, num_petals, price):
        self.name = name
        self.num_petals = num_petals
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_num_petals(self): 
        return self.num_petals;
   
    def get_price(self):
        return self.price;


flowers = Flower("lilac", 27, 15.99)

print(flowers.get_name())
print(flowers.get_num_petals())
print(flowers.get_price())
