# def hello():
#     print('Hello') 
#     print('Goodbye!')

FLAT_SHIPPING: 10
TAX_RATE = 0.1

def add_tax(amount):
        return amount * (1 + TAX_RATE)

def add_shipping(amount):
        return amount + FLAT_SHIPPING

def calc_grant_total(amount):
        return add_tax(add_shipping(amount))

#Main

subtotal = float(input('Subtotal: $'))
grand_total = calc_grant_total(subtotal)
print(f'Total: ${grand_total: .2f}') 

