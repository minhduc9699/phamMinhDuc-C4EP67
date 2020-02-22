from getpass import getpass
username = 'mindx'
password = 'xdnim'

loop = True
count = 0
while loop:
  count += 1
  if count == 7:
    print('spam vừa thôi T.T')
    loop = False
  else:
    input_username = input('username?')
    if input_username == username:
      input_password = getpass()
      if input_password == password:
        print('Welcome to mindx')
        loop = False
      else:
        print('wrong password')
    else:
      print('wrong username')