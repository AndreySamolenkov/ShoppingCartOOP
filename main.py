class ShoppingCart:

  def __init__(self):
    self.__cart = {}

  def add_item(self, name, price):
    self.__cart[name] = price
    return f'{name} with the price of ${price:.2f} has been added to your cart'

  def remove_item(self, name):
    if name not in self.__cart:
      return f'{name} is not in the cart.'
    self.__cart.pop(name)
    return f'{name} has been removed from your cart.'

  def display_cart(self):
    if not self.__cart:
      return 'The cart is empty. Add items first.'
    result = 'There are the following items in your cart:\n\n'
    total = 0
    for name, price in self.__cart.items():
      total += price
      result += f'{name}, ${price:.2f}\n'
    return f'{result}\nTotal: ${total:.2f}\n'


my_cart = ShoppingCart()
my_cart.add_item('sausages', 3.99)
my_cart.add_item('tomatoes', 5.00)
my_cart.add_item('milk', 2.69)
my_cart.add_item('coffee beans', 8.99)

print(my_cart.display_cart())

my_cart.remove_item('milk')

print(my_cart.display_cart())