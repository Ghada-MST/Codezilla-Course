

item_code = input('Enter the code of the item: ')
price = float(input('Enter the price of the item: '))

#items and sales
sales_70_items = ['070','170','270','370','470']
sales_50_items = ['050','150','250','350','450']
sales_30_items = ['030','130','230','330','430']



if item_code in sales_70_items:
  price = price-(price * 0.70)
  percent = 70
elif item_code in sales_50_items:
  price = price-(price * 0.50)
  percent = 50
elif item_code in sales_30_items:
  price = price-(price * 0.30)
  percent = 30
else:
  percent = 0
  
print(f'The final price of item code-{item_code} after {percent:.1f}% sale is {price:,.2f} EGP')


#حل المهندس اسلام


item_code = input('Enter the code of the item: ')
price = float(input('Enter the price of the item: '))

#items and sales
sales_70_items = ['070','170','270','370','470']
sales_50_items = ['050','150','250','350','450']
sales_30_items = ['030','130','230','330','430']


if item_code in sales_70_items:
  sale_amount = 0.70
elif item_code in sales_50_items:
  sale_amount = 0.50
elif item_code in sales_30_items:
  sale_amount = 0.30
else:
  sale_amount = 0

price*= (1-sale_amount)
  
print(f'The final price of item code-{item_code} after {sale_amount*100}% sale is {price:,.2f} EGP')