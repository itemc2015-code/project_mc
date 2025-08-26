<<<<<<< HEAD
print('Shopping cart')
=======

import json
import os

# with open('cart_list.json','r') as f:
#     lists = json.load(f)

menu_lists = []
class Order:
    def __init__(self,numbers=None,counts=None,stored=None):
        self.numbers = numbers
        self.counts = counts
        self.stored = stored
        self.counts = 0
        self.numbers = 0
        self.order_lists = []
        self.order_storage = []

        with open('cart_list.json', 'r') as f:
            self.lists = json.load(f)
        # with open('order_lists.json','w') as f:
        #     json.dump(self.order_storage,f,indent=4)
    def menus(self):
        # with open('order_lists.json','w') as f:
        #     json.dump(self.order_storage,f,indent=4)
        print('\n    🛒 WELCOME TO SHOPPING CART ONLINE 🛒')
        print(f"{'NO.'}{'📃 ITEM':>17}{'💲PRICE':>20}")
        print('-' * 48)
        for num, l1 in enumerate(self.lists):
            menulists1 = num + 1, l1['item'], l1['price']
            menu_lists.append(menulists1)
            print(f"{num + 1:<10}       {l1['item']:<15}      ${str(l1['price']):<9}")
        print()
    def orders(self,customer_orders=None):
        while True:
            customer_orders = input('\nNumber to add to cart🛒 or "q" to quit: ')
            if customer_orders == 'q':
                print('Thank you for shopping 🛒\n')
                self.order_storage.clear()
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
        total_price = 0
        total_items = 0
        if os.path.exists('order_lists.json'):
            if os.path.getsize('order_lists.json') == 0:
                print("=============== Orders =============")
                print('                Empty               ')
            else:
                with open('order_lists.json','r') as f:
                    save_orders = json.load(f)
                    print("\n============= Orders =============")
                    print(f'{"ITEM":>5}{"PRICE":>13}{"QTY":>13}{"TOTAL":>13} ')
                    for v in save_orders:
                        print(f'{v["item"].ljust(13)}${str(v["price"]).ljust(14)}{str(v["count"]).ljust(10)} {v["count"]*v["price"]}')
                        total_price += int(v["count"]) * int(v["price"])
                        total_items += int(v["count"])
                    print(f'Total Order: ${total_price}')
                    print(f'Total Items: {total_items} ')
        else:
            print('File not found')

order1 = Order()
order1.menus()
order1.orders()

'''
cash and changes
debit or credit
cash or atm
'''





>>>>>>> c90f97bc833b1eca65c9da9a0aa440e5bbd1a3f3
