# def hello():
#     print('Hello') 
#     print('Goodbye!')

def add_gst(amount):
        total = amount * 1.1
        return total


subtotal = float(input('Subtotal: $'))
grand_total = add_gst(subtotal)
print(f'Total: ${grand_total: .2f}') 

