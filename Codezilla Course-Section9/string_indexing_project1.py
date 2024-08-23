full_name = input('Enter your full name: ').strip().capitalize()

space_idx = full_name.index(' ')

first_name = full_name[:space_idx]

print(f'''Hello, {first_name}!
Welcome at Codezilla''')

