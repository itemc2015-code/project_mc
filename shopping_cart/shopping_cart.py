import json
import os
import time

menu_lists = []
class Order:
    def __init__(self,numbers=None,counts=None,stored=None):
        self.numbers = numbers
        self.counts = counts
        self.stored = stored
        self.menu_lists = menu_lists
        self.counts = 0
        self.numbers = 0
        self.order_lists = []
        self.order_storage = []
        self.total_price = 0
        self.subtotal = 0
        self.total_items = 0


        with open('cart_list.json', 'r') as f:
            self.lists = json.load(f)

    def menus(self):
        print('\n    🛒 WELCOME TO SHOPPING CART ONLINE 🛒')
        print(f"{'NO.'}{'📃 ITEM':>17}{'💲PRICE':>20}")
        print('-' * 48)
        for num, l1 in enumerate(self.lists):
            menulists1 = num + 1, l1['item'], l1['price']
            self.menu_lists.append(menulists1)
            print(f"{num + 1:<10}       {l1['item']:<15}      ${str(l1['price']):<9}")
        print()

    def orders(self,customer_orders=None):
        while True:
            customer_orders = input('Number to add to cart🛒, "q" for done: ')
            if customer_orders == 'q':
                self.order_storage.clear()
                break
            elif customer_orders == 'd':
                print('===SUMMARY===')
                break
            try:
                customer_orders = int(customer_orders)
                self.counts = int(input('Count: '))
                if 1 <= customer_orders <= len(menu_lists):
                    self.order_lists.append(menu_lists[customer_orders-1])
                    self.list_order()
                else:
                    print(f'❌ Invalid, {customer_orders} Not found')
            except ValueError:
                print('❌ Invalid input')
                continue
    def list_order(self):
        for num,o in enumerate(self.order_lists):
            self.stored = {"no":num+1,"item":o[1],"price":o[2],"count":self.counts}
        self.order_storage.append(self.stored)
        with open('order_lists.json','w') as f:
            json.dump(self.order_storage,f,indent=4)
        self.view_order()

    def view_order(self):
        if os.path.exists('order_lists.json'):
            if os.path.getsize('order_lists.json') == 0:
                print("=============== Orders =============")
                print('                Empty               ')
            else:
                self.total_price = 0
                self.total_items = 0
                with open('order_lists.json','r') as f:
                    save_orders = json.load(f)
                    print("\n================== Shopping Cart ==================")
                    print(f'{"ITEM":>5}{"PRICE":>15}{"QTY":>13}{"TOTAL":>13} ')
                    for v in save_orders:
                        print(f'{v["item"].ljust(15)}${v["price"]:<14,.2f}{str(v["count"]).ljust(10)} ${v["count"]*v["price"]:,.2f}')
                        self.total_price += int(v["count"]) * int(v["price"])
                        self.total_items += int(v["count"])
                    print('=====================================================')
                    print(f'Sub Total: ${self.total_price:,.2f}')
                    print(f'Total Items: {self.total_items} ')
                    print()
        else:
            print('File not found')

class Discount(Order):
    def __init__(self,total_discount=None,discount_type=None):
        super().__init__(numbers=None,counts=None,stored=None)
        self.total_discount = total_discount
        self.discount_type = discount_type
        self.discount_type_list = {"1": 0.05, "2": 0.1, "3": 0.2}
    def discount(self):
        normal_discount = 0.05
        member_discount = 0.1
        senior_discount = 0.2
        while True:
            disc = input('Discount (y/n): ').lower()
            if disc == 'y':
                self.discount_type = input('\n1.Normal\n2.Member\n3.Senior\nDiscount type (1-3): ')
                if self.discount_type in self.discount_type_list:
                    rate = self.discount_type_list[self.discount_type]
                    self.total_discount = self.total_price * rate
                    self.total_discount_price = self.total_price - self.total_discount
                    print(f'Discount({rate*100:.0f}%): ${self.total_discount:,.2f}')
                    break
                else:
                    print('Invalid ❌')
            elif disc == 'n':
                 self.total_discount = 0.00
                 self.total_discount_price = self.total_price
                 break
            else:
                print('Invalid ❌')

class Vat(Discount):
    def __init__(self,taxes=0,vat=0):
        super().__init__(total_discount=None,discount_type=None)
        self.grandtotal = taxes
        self.vat = vat
        self.vat_type = {"1": 0.2, "2": 0.1, "3": 0.05}
    def cal_tax(self):
        if self.discount_type in self.vat_type:
            rate = self.discount_type_list[self.discount_type]
            self.vat = self.total_price * self.vat_type[self.discount_type]
            self.grandtotal = self.total_price-((self.total_price + self.vat)*rate)
        else:
            self.total_discount = 0.00
            self.discount_type = 0.00
class Payment(Vat):
    def __init__(self):
        super().__init__(taxes=0)
    def cash(self,userpayment=None):
        self.userpayment = userpayment
        self.discount()
        while True:
            try:
                self.userpayment = int(input('Cash: $'))
                if self.userpayment < self.total_discount_price:
                    print('❌Insufficient fund')
                    continue
                else:
                    os.system('cls')
                    total = self.userpayment - self.total_discount_price
                    with open('order_lists.json', 'r') as f:
                        save_orders = json.load(f)
                        print("\n================== Shopping Cart ==================")
                        print(f'{"ITEM":>5}{"PRICE":>15}{"QTY":>13}{"TOTAL":>13} ')
                        for v in save_orders:
                            print(f'{v["item"].ljust(15)}${v["price"]:<14,.2f}{str(v["count"]).ljust(10)} ${v["count"] * v["price"]:,.2f}')
                    print('=====================================================')
                    print(f'Sub Total: ${self.total_price:,.2f}')

                    if self.discount_type in self.discount_type_list:
                        discount_type_output = self.discount_type_list[self.discount_type]
                        print(f'Discount({discount_type_output*100:.0f}%): -${self.total_discount:,.2f}')
                    else:
                        self.discount_type = 0.00

                    self.cal_tax()
                    print(f'Tax: ${self.vat:,.2f}({self.vat_type[self.discount_type]*100:.0f}%)')
                    print(f'Grand Total: ${self.grandtotal:,.2f}')
                    print(f'Total Items: {sum((v["count"]) for v in save_orders)} ')
                    print(f'Cash: ${self.userpayment:,.2f}')
                    print(f'Change: ${total:,.2f}')
                    print('               -------------------------    ')
                    print('                Thank you for shopping 🛒\n')
                    self.total_price = 0
                    self.total_items = 0
                    break
            except ValueError:
                print(f'{self.userpayment} is invalid')

if __name__ == "__main__":

    order1 = Order()
    order1.menus()
    order1.orders()

    if order1.total_price > 0:
        pay1 = Payment()
        pay1.total_price = order1.total_price
        pay1.cash()
    else:
        print('\nExiting...\n')

'''
'''
