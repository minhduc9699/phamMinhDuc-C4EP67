# list
mon_an = ['trứng', 'cơm', 'cá'] # initialize
print(*1)
new_item = 'thỏ'
mon_an.append(new_item) # Create

item = mon_an[0]
mon_an[0] = 'thỏ' # Update
mon_an[2] = item

mon_an.pop(1) # Delete
mon_an.remove('trứ') # Delete

print('trứng' in mon_an)

for i in range(len(mon_an)):
  print(i+1, mon_an[i]) # Read 

for value in mon_an: # Read
  print(value)