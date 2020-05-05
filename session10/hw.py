from flask import *
from pymongo import MongoClient

client = MongoClient()
db = client.get_database('c4e')
kpop_collection = db.get_collection('Kpop')


app = Flask(__name__)


# @app.route('/about-me')
# def about_me():
#   return 'this is me'


@app.route('/about-me')
def about_me():
  return render_template('about_me.html')

@app.route('/school')
def school():
  return redirect('https://mindx.edu.vn/')

@app.route('/bmi/<weight>/<height>')
def bmi(weight, height):
  weight = float(weight)
  height = float(height)
  bmi = weight / (height/100)**2
  
  if bmi < 16:
    return 'you need some food!'
  elif bmi < 18.5:
    return 'Underweight'
  elif bmi < 25:
    return 'Hello normal'
  elif bmi < 30:
    return 'Overweight'
  else:
    return 'Obese'

@app.route('/user/<username>')
def user(username):
  client = MongoClient()
  db = client.get_database('c4e')
  kpop_collection = db.get_collection('Kpop')

  user = kpop_collection.find_one({
    '$or': [
      {'stage_name': username},
      {'full_name': 'aa'}
    ]
  })
  
  if user is not None:
    return render_template(
      'user.html', 
      name=user['stage_name'], 
      full_name=user['full_name']
    )
  else:
    return 'NOT FOUND'



app.run(debug=True, port=3000)