
pizzas = [
'Margherita',
'Pepperoni',
'Super Supreme',
'Hawaiian',
'Meat Lovers',
'Cheese Lovers'
]
# a message to ask the user for the pizza
message = f"""
Please, Enter the number of the pizza you want to order:
1. {pizzas[0]}
2. {pizzas[1]}
3. {pizzas[2]}
4. {pizzas[3]}
5. {pizzas[4]}
6. {pizzas[5]}
"""
# get the pizza index
order_index = int(input(message))
n_pizza = input("Enter the number of pizzas you want: ")
print('-' * 50)
# get the pizza from list
order = pizzas[order_index - 1]
# print the order
order_message = f"""Please, Enjoy your time
While we get {n_pizza} {order} pizza ready for you."""
print('Thanks for choosing Codezillas Pizza!')
print(order_message)