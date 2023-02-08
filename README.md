Shopping Cart

This is a class implementation of a shopping cart, which allows users to add items, remove items, and display the contents of the cart.
Class methods:

    add_item(self, name, price): Adds an item to the cart with the given name and price. Returns a message indicating the item has been added.
    remove_item(self, name): Removes the item with the given name from the cart. Returns a message indicating the item has been removed.
    display_cart(self): Displays the contents of the cart, including the names and prices of each item, as well as the total price. I
    f the cart is empty, returns a message indicating the cart is empty.

Example Usage:

my_cart = ShoppingCart()
my_cart.add_item('sausages', 3.99)
my_cart.add_item('tomatoes', 5.00)
my_cart.add_item('milk', 2.69)
my_cart.add_item('coffee beans', 8.99)

print(my_cart.display_cart())

my_cart.remove_item('milk')

print(my_cart.display_cart())

Output:

There are the following items in your cart:

sausages, $3.99
tomatoes, $5.00
milk, $2.69
coffee beans, $8.99

Total: $20.67

There are the following items in your cart:

sausages, $3.99
tomatoes, $5.00
coffee beans, $8.99

Total: $18.98
