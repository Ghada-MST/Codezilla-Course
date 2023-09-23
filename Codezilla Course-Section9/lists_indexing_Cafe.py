# a list of hot drinks, soda, and juices
total_drinks = [
['Tea', 'Herbs', 'Hot Cider', 'Coffee', 'Hot Chocolate'],
['Coke', 'Pepsi', 'Fanta', 'Sprite', 'Mirinda'],
['Lemonade', 'Orange Juice', 'Mango Juice',
'Strawberry Juice', 'Apple Juice']
]
drinks_type = ['Hot drinks','Soda','Juices']

intro_message = f"""
Codezilla cafe main menu:
1.{drinks_type[0]}
2.{drinks_type[1]}
3.{drinks_type[2]}

Please, Enter the type of the drink you want to order: """

order_index = int(input(intro_message))
order_type = order_index - 1

mid_message = f""" 
{drinks_type[order_type]} menu:
1.{total_drinks[order_type][0]}
2.{total_drinks[order_type][1]}
3.{total_drinks[order_type][2]}
4.{total_drinks[order_type][3]}
5.{total_drinks[order_type][4]}

Please, Enter the number of the drink you want to order: """ 

order_nest = int(input(mid_message))
order_num = order_nest - 1

print('-'*50)

end_message = f"""
Thanks for choosing Codezillas Cafe!
Please, Enjoy your time
While we get {total_drinks[order_type][order_num]} ready for you
"""

print(end_message)
