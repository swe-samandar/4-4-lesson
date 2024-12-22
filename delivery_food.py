import random, os

os.system("clear")
# Dastur haqida deliveryFood.txt faylda tushuntirib o'tilgan.

class Dishes:
    menu = dict()
    def __init__(self, dish_name, price):
        self.dish_name = dish_name
        self.price = price
        Dishes.menu.update({dish_name: price})
        
    @staticmethod
    def show_menu():
        return [dish for dish in Dishes.menu]


class Customers:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.made_order = False

    def make_order(self):
        if all(deliever.task for deliever in Delivers.delievers):
            print("Hozirda hamma yetkazib beruvchilarimiz band ekan keyinroq urinib ko'ring!")
            return

        order = Orders(self)
        while Delivers.delievers:
            deliever = random.choice(Delivers.delievers)
            if not deliever.task:
                deliever.task = order.order_id
                self.deliever = deliever
                print(f"""Sizning buyurtmangiz qabul qilindi.
YETKAZIB BERUVCHI ISMI:          {deliever.deliever_name}
YETKAZIB BERISH VOSITASI RAQAMI: {deliever.vehicle_number}""")
                break

    def give_order(self):
        if self.made_order in Orders.orders:
            Orders.orders.remove(self.made_order)
            self.made_order = False
            self.deliever.task = False
            print("Buyurtma yetkazib berildi.")
        else:
            print("Siz hech qanday buyurtma qilmagansiz!")


class Orders:
    orders = []
    def __init__(self, customer):
        print(f"Bizda mavjud bo'lgan taomlar ro'yxati: {Dishes.show_menu()}")
        while True:
            id = random.randint(1000,9999)
            if id not in Orders.orders:
                self.order_id = id
                Orders.orders.append(id)
                break

        selected_dishes = (input("Buyurtma qilmoqchi bo'lgan taomlaringizni kiriting: ")).split(", ")
        self.selected_dishes = selected_dishes
        self.total_price = sum([Dishes.menu.get(dish, 0) for dish in selected_dishes])
        print(f"Buyurtmaning umumiy narxi {self.total_price} so'm bo'ladi.")
        customer.made_order = id


class Delivers:
    delievers = []
    def __init__(self, deliever_name, vehicle_number):
        self.deliever_name = deliever_name
        self.vehicle_number = vehicle_number
        self.task = False
        Delivers.delievers.append(self)



dish1 = Dishes("Osh", 35_000)
dish2 = Dishes("Beshbarmoq", 60_000)
dish3 = Dishes("Norin", 20_000)

deliever1 = Delivers("Abror", "01 A 100 AA")
deliever2 = Delivers("Kamron", "01 C 777 CC")
deliever3 = Delivers("Kamron", "01 B 777 BB")


customer1 = Customers("Olim", "+998901234567")
customer2 = Customers("Anvar", "+998911112233")

customer1.make_order()
customer2.make_order()

customer1.give_order()
customer2.give_order()