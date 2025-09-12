#shopping cart v2

import json
import os
import time

#menu_lists = []

class Order:
    def __init__(self,numbers=None,counts=None,stored=None):
        self.numbers = numbers
        self.counts = counts
        self.stored = stored
        self.menu_lists = []
        self.counts = 0
        self.numbers = 0
        self.order_lists = []
        self.order_storage = []
        self.total_price = 0
        #self.subtotal = 0
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
            customer_orders = input('Number to add to cart🛒, "d"/delete, "q"/done: ')
            if customer_orders == 'q':
                self.order_storage.clear()
                break
            elif customer_orders == 'd':
                if len(self.order_lists) == 0:
                    print('Cart is empty 🛒')
                    continue
                else:
                    if input('Proceed deleting (y or any key to exit): ').lower().strip() == 'y':
                        self.delete_order()
                        break
                    else:
                        continue
            try:
                customer_orders = int(customer_orders)
                self.counts = int(input('Count: '))
                if 1 <= customer_orders <= len(self.menu_lists):
                    self.order_lists.append(self.menu_lists[customer_orders-1])
                    self.list_order()
                else:
                    print(f'❌ Invalid, {customer_orders} Not found')
            except ValueError:
                print('❌ Invalid input')
                continue
    def list_order(self):
        order_number = 0
        o = self.order_lists[-1]
        numbering = len(self.order_lists)
        self.stored = {"no":numbering,"item":o[1],"price":o[2],"count":self.counts}
        numbering[0]
        self.order_storage.append(self.stored)
        with open('order_lists.json','w') as f:
            json.dump(self.order_storage,f,indent=4)
        self.view_order()

        # for num,o in enumerate(self.order_lists):
        #     self.stored = {"no":num+1,"item":o[1],"price":o[2],"count":self.counts}
        # self.order_storage.append(self.stored)
        # with open('order_lists.json','w') as f:
        #     json.dump(self.order_storage,f,indent=4)
        # self.view_order()

    def view_order(self):
        if os.path.exists('order_lists.json'):
            if os.path.getsize('order_lists.json') == 0:
                print("=============== Orders =============")
                print('                Empty               ')
            else:
                self.total_price = 0
                self.total_items = 0
                with open('order_lists.json','r') as f:
                    #save_orders = json.load(f)
                    try:
                        save_orders = json.load(f)
                        print("\n==================== Shopping Cart =====================")
                        print(f'{"ITEM":>8}{"PRICE":>20}{"QTY":>10}{"TOTAL":>13} ')
                        for v in save_orders:
                            print(f'{v["no"]:<3}{v["item"].ljust(19)}${v["price"]:<13,.2f}{str(v["count"]).ljust(8)} ${v["count"]*v["price"]:,.2f}')
                            self.total_price += int(v["count"]) * int(v["price"])
                            self.total_items += int(v["count"])
                        print('========================================================')
                        print(f'Sub Total: ${self.total_price:,.2f}')
                        print(f'Total Items: {self.total_items} ')
                        print()
                    except:
                        print('Invalid, Not found')

        else:
            print('File not found')
    def delete_order(self):
        is_running = True
        while is_running:
            try:
                remove_item = int(input('Remove item: '))
                if 1 <= remove_item <= len(self.order_storage):
                    self.order_storage.pop(remove_item-1)
                    self.total_price = 0
                    self.total_items = 0

                    #print(self.order_storage) #for out put checking only
                    with open('order_lists.json','w+') as f:
                        json.dump(self.order_storage,f,indent=4)
                        print("\n==================== Shopping Cart =====================")
                        print(f'{"ITEM":>8}{"PRICE":>20}{"QTY":>10}{"TOTAL":>13} ')
                        for num, v in enumerate(self.order_storage):
                            print(f'{num+1:<3} {v["item"].ljust(19)}${v["price"]:<12,.2f}{str(v["count"]).ljust(8)} ${v["count"] * v["price"]:,.2f}')
                            self.total_price += int(v["count"]) * int(v["price"])
                            self.total_items += int(v["count"])
                        print('========================================================')
                        print(f'Sub Total: ${self.total_price:,.2f}')
                        print(f'Total Items: {self.total_items} ')
                        print()
                        self.orders()
                        self.total_price = 0
                        self.total_items = 0
                        #is_running = False

                else:
                    print('Not found ❌')
            except ValueError:
                print('Invalid ❌')

class Discount(Order):
    def __init__(self,total_discount_price=None,total_discount=None,discount_type=None,have_discount=None):
        super().__init__(numbers=None,counts=None,stored=None)
        self.total_discount = total_discount
        self.discount_type = discount_type
        self.have_discount = have_discount
        self.total_discount_price = total_discount_price
        self.discount_type_list = {"0":0.00,"1": 0.05, "2": 0.1, "3": 0.2}
    def discount(self):
        while True:
            self.have_discount = input('Discount (y/n): ').lower()
            if self.have_discount == 'y':
                self.discount_type = input('\n1.Normal\n2.Member\n3.Senior\nDiscount type (1-3): ')
                if self.discount_type in self.discount_type_list:
                    rate = self.discount_type_list[self.discount_type]
                    self.total_discount = self.total_price * rate
                    discount_price = self.total_price - self.total_discount
                    self.total_discount_price = discount_price
                    break
                else:
                    print('Invalid ❌')
            elif self.have_discount == 'n':
                 self.total_discount = 0.00
                 self.discount_type = "0"
                 self.total_discount_price = self.total_price
                 break
            else:
                print('Invalid ❌')

class Vat(Discount):
    def __init__(self,vat=0,grandtotal=0):
        super().__init__(total_discount_price=None,total_discount=None,discount_type=None,have_discount=None)
        self.grandtotal = grandtotal
        self.vat = vat
        self.taxes = 0.05
    def cal_tax(self):
        self.vat = self.total_discount_price * self.taxes
        self.grandtotal = self.total_discount_price + self.vat

class Payment(Vat):
    def __init__(self):
        super().__init__(vat=0,grandtotal=0)
    def cash(self,userpayment=None):
        discount_type_output = self.discount_type_list[self.discount_type]
        #self.cal_tax()
        self.view_order()
        #print(f'\nDiscount({discount_type_output * 100:.0f}%): -${self.total_discount:,.2f}')
        print(f'Discount({discount_type_output * 100:.0f}%):-${self.total_discount:,.2f}'
              if discount_type_output > 0 else 'Discount:(N/A)')
        print(f'Tax(5%): ${self.vat:.2f}')
        print(f'Grand Total: ${self.grandtotal:,.2f}')
        print(f'Total Items: {self.total_items} ')
        print(f'Grand Total: ${self.grandtotal:,.2f}')

        while True:
            try:
                self.userpayment = int(input('Cash: $'))
                if self.userpayment < self.grandtotal:
                    print('❌Insufficient fund')
                    continue
                else:
                    os.system('cls')
                    total = self.userpayment - self.grandtotal
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
                        #print(f'Discount({discount_type_output*100:.0f}%): -${self.total_discount:,.2f}')
                        print(f'Discount({discount_type_output * 100:.0f}%):-${self.total_discount:,.2f}'
                              if discount_type_output > 0 else 'Discount:(N/A)')
                    else:
                        self.discount_type = 0.00

                    self.cal_tax()
                    print(f'Tax(5%): ${self.vat:.2f}')
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

    def order_again(self):
        while True:
            again = input('Enter another order (y/n): ').lower().strip()
            if again == 'y':
                self.order_lists.clear()
                self.menus()
                self.orders()
                self.discount()
                self.cash()
            elif again == 'n':
                print('                \nThank you for shopping 🛒')
                print('Goodbye 👋\n')
                break
            else:
                print('Invalid input')

if __name__ == "__main__":

    pay1 = Payment()
    pay1.menus()
    pay1.orders()
    pay1.discount()
    pay1.cal_tax()

    if pay1.total_price > 0:
        #pay1.discount()
        pay1.cal_tax()
        pay1.cash()
        pay1.order_again()
    else:
        print('\nExiting...\n')

