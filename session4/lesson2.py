# age = 10
# name = 'Mai'
# if age >= 18 or name == 'Mai':
#   print('Welcome to p**h**')
# elif age == 18:
#   print('Đợi thêm 1 năm nữa e ơi')
# else:
#   print('Bố mẹ em đâu?')
# number = input()
# print(int(number)**2)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4*a*c
if delta > 0:
  x1 = (-b + delta**0.5)/(2*a)
  x2 = (-b - delta**0.5)/(2*a)
  print(f"x1 = {x1} x2 = {x2}")  # f = formart
elif delta == 0:
  x = (-b)/(2*a)
  print("x =",x)
else:
  print("PT vo nghiem")
