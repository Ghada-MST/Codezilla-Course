text = """A computer is a digital electronic machine 
that can be programmed to carry out sequences of 
arithmetic or logical operations automatically"""

characters_with_spaces = len(text)

characters_without_spaces = len(text.replace(' ',''))

print(f'Number of character with spaces is {characters_with_spaces}')

print(f'Number of character without spaces is {characters_without_spaces}')