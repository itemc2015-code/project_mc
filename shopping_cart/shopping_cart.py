
import json

with open('cart_list.json','r') as f:
    lists = json.load(f)
    #print(lists)

menu_lists = []
order_lists = []

class Order:
    def __init__(self,numbers=None,counts=None):
        self.numbers = numbers
        self.counts = counts
    def menus(self):
        print('\n    🛒 WELCOME TO SHOPPING CART ONLINE 🛒')
        print(f"{'NO.'}{'📃 ITEM':>17}{'💲PRICE':>20}")
        print('-' * 48)
        for num, l1 in enumerate(lists):
            menulists1 = num + 1, l1['item'], l1['price']
            menu_lists.append(menulists1)
            print(f"{num + 1:<10}       {l1['item']:<15}      ${str(l1['price']):<9}")
            #print(self.menulists) #testing for menu_lists output(tuple)
        print()
    def orders(self,customer_orders=None):
        while True:
            try:
                customer_orders = int(input('\nNumber to add to cart🛒 or "q" to quit: '))
                if 1 <= customer_orders <= len(menu_lists):
                    print("\nOrder added:")
                    order_lists.append(menu_lists[customer_orders-1])
                    self.list_order()
                    #print(order_lists) ##check if the order list is correct
                    #print(menu_lists[customer_orders-1]) ##check if the order is correct
                else:
                    print(f'Invalid, {customer_orders} Not found')
            except ValueError:
                print('Invalid input')
                continue
    def list_order(self):
        total_price = 0
        print(f'{'ITEM':>8}{'PRICE':>13} ')
        for num,o in enumerate(order_lists):
            print(f'{num + 1}. {o[1]} ------ ${o[2]:<10.2f}')
            total_price += o[2]
        print(f'💸TOTAL: ${total_price}')


order1 = Order()
order1.menus()
order1.orders()

