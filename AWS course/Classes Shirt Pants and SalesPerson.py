class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)

new_shirt = Shirt('red', 'S', 'short sleeve', 15)
#print new_shirt.color
#print new_shirt.price

new_shirt.change_price(10)
#print new_shirt.price
#print new_shirt.discount(.2)


class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = float(price)

    def change_price(self, new_price):
        self.price = float(new_price)

    def discount(self, discount):
        return self.price*(1-discount)

jeans = Pants('blue', 30, 32, 100)
slaks = Pants('black', 32, 33, 50)


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary, pants_sold, total_sales):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.employee_id = int(employee_id)
        self.salary = float(salary)
        self.pants_sold = []
        self.total_sales = 0.0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)
        self.total_sales += 1

    def display_sales(self):
        for i in range(len(self.pants_sold)):
            print "color:", self.pants_sold[i].color, "waist_size:", self.pants_sold[i].waist_size, "length:", self.pants_sold[i].length, "price:", self.pants_sold[i].price

    def calculate_sales(self):
        total = 0.0
        for i in range(len(self.pants_sold)):
            total += self.pants_sold[i].price
        return total

    def calculate_commission(self, percentage):
        total = self.calculate_sales()
        return total*percentage

jo = SalesPerson('Jo', 'Shmo', 007, 5000, [], 0)
jo.sell_pants(jeans)
jo.sell_pants(slaks)

jo.display_sales()
print jo.total_sales
