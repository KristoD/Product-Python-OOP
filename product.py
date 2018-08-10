class Products(object):

    def __init__(self, price, name, weight, brand, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.final_price = self.price * tax
        self.final_price = self.final_price + self.price
        self.price = self.final_price
        return self
    
    def returns(self, reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
            return self
        elif reason == "new":
            self.status = "for sale"
            return self
        elif reason == "opened":
            self.status = "used"
            self.discount = self.price * 0.20
            self.discount = self.price - self.discount
            self.price = self.discount
            return self
    
    def display_info(self):
        print "Price: " + str(self.price)
        print "Item Name: " + self.name
        print "Weight: " + str(self.weight)
        print "Brand: " + self.brand
        print "Status: " + self.status
        return self

product1 = Products(200, "Shit Vape", 2, "Smok").add_tax(0.10).returns("defective").display_info()
product2 = Products(200000, "Aventador", 3500, "Lamborghini").add_tax(0.20).display_info()
product3 = Products(2000, "MacBook Pro", 10, "Apple").add_tax(0.15).returns("new").display_info()
product4 = Products(2000000000, "iPhone X", 3, "Apple").add_tax(0.50).returns("opened").display_info()
print product1, product2, product3, product4


