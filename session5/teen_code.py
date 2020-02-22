teen_code = {
  'vk': 'vợ',
  'ck': 'chồng',
  'hok': 'không',
  'hoy': 'thôi',
  'clgt': 'củ lạc giòn tan'
}

loop = True
while loop:
  word = input('nhập từ teencode bạn muốn tra').strip()
  if word in teen_code:
    print(word, 'có nghĩa là: ', teen_code[word])
  else:
    ans = input('từ trên không có trong từ điển, bạn có muốn bổ sung không? (y/n)').lower().strip()
    if ans == 'y':
      new_word = input('mời bạn nhập nghĩa của từ đó')
      teen_code[word] = new_word
    elif ans == 'n':
      print('bye bye')
      loop = False
