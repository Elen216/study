class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions
    def __str__(self):
        return f"{self.name} ({self.dimensions}) - {self.price} грн"
class Customer:
    def __init__(self, first_name, last_name, middle_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name} (тел.: {self.phone}"
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = [] 
    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def __str__(self):
        order_details = f"Замовлення для: {self.customer}\nТовари:\n"
        for item in self.items:
            prod = item["product"]
            qty = item["quantity"]
            order_details += f"- {prod.name} x {qty} шт. = {prod.price * qty} грн\n"
        order_details += f"Загальна вартість: {self.calculate_total()} грн"
        return order_details
