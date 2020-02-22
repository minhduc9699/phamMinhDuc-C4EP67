quizzes = [
  {
    'question': 'con nhện có mấy chân?',
    'choices': [
      '2 chân',
      '4 chân',
      '6 chân',
      '8 chân'
    ],
    'right_awnser': 3
  },
  {
    'question': 'con chó có mấy chân?',
    'choices': [
      '2 chân',
      '4 chân',
      '6 chân',
      '8 chân'
    ],
    'right_awnser': 1
  }
]

for quiz in quizzes:
  print(quiz['question'])
  choices = quiz['choices']
  for i in range(len(choices)):
    print(f'{i+1}. {choices[i]}') # string formart
  user_choice = int(input('trả lời đê!!')) - 1
  if user_choice == quiz['right_awnser']:
    print('bạn giỏi thật!!')
  else:
    print('bạn sai mất rồi')


# for i in range(len(quizzes)):
#   print(quizzes[i]['question'])