# person = ['Đức', 96, 'Hà Nội', 'Sơn La', 'dev', False, True]

person = {
  'name': 'Đức', 
  'yob': 96, 
  'address': '...',
}

person['gender'] = 'Male' # Create
person['address'] = 'Đà Lạt' # Update
del person['yob'] # Delete
if 'name' in person:
  print(person['name'])
# READ All
key = input()
print(person[key])
# for key, value in person.items(): 
#   print(key, value)