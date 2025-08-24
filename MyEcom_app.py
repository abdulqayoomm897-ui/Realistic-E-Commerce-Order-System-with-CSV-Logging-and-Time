from datetime import datetime as dt

class Order:
    discount = 0 

    def __init__(self):
        self.items = []   # it Stores id, name, price and quantity

    # --------- Decorator ---------
    def logger(func):
        def wrapper(*args, **kwargs):
            with open("log.txt", "a") as log_file:
                log_file.write(f"{dt.now()} Running..'{func.__name__}'...\n")

            result = func(*args, **kwargs)

            with open("log.txt", "a") as log_file:
                log_file.write(f"{dt.now()} Finished..'{func.__name__}'...\n")

            return result
        return wrapper

    # --------- Instance Methods ---------
    @logger
    def add_item_by_id(self, product_id, quantity):
        with open("products.csv", "r") as f:
            products = [line.strip().split(',') for line in f.readlines()]

        products.pop(0)  # remove header

        for pid, name, price in products:
            if int(pid) == product_id:
                self.items.append((int(pid), name, float(price), quantity))
                print(f"Added {quantity} × {name} (ID {pid})")
                return
        print(f"Product ID {product_id} not found!")

    def calculate_total(self):
        subtotal = sum(price * qty for _, _, price, qty in self.items)
        return subtotal - (subtotal * Order.discount / 100)

    @classmethod
    def set_discount(cls, discount_rate):
        cls.discount = discount_rate


# ---------------- Testing ----------------
if __name__ == "__main__":
    order = Order()
    order.add_item_by_id(1, 2)  
    order.add_item_by_id(4, 3)  
    order.add_item_by_id(99, 1) 

    Order.set_discount(10)

    total = order.calculate_total()
    print("Final total:", total)
