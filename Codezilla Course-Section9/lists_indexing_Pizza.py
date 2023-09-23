
pizzas = [
'Margherita',
'Pepperoni',
'Super Supreme',
'Hawaiian',
'Meat Lovers',
'Cheese Lovers'
]

message = f"""
The menu of our delicious pizza 

1.{pizzas[0]}
2.{pizzas[1]}
3.{pizzas[2]}
4.{pizzas[3]}
5.{pizzas[4]}
6.{pizzas[5]}

Please, Enter the number of the pizza you want to order from the menu : """

order_index = int(input(message))
order = order_index - 1

num_pizza = input('\nEnter the number of pizzas you want: ')

print('-'*40)

end_message = f"""Thanks for choosing codezillas Pizza!
Please, Enjoy your time
While we got {num_pizza} {pizzas[order]} pizza ready for you."""

print(end_message)


