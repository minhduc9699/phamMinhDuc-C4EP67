from random import randint, choice
from calc import calc

a = randint(0, 9)
b = randint(0, 9) 
operators_poll = ['+', '-', '*', '/']
operator = choice(operators_poll)
result = calc(a, b, operator)
random_num = randint(-1, 1)
display_result = result + random_num
print(f'{a} {operator} {b} = {display_result}')
choice = input('T/F')
if random_num == 0:
  if choice == 'T':
    print('yayyy')
  else:
    print('sai cmnr')
else:
  if choice == 'F':
    print('yayyy')
  else:
    print('sai cmnr')