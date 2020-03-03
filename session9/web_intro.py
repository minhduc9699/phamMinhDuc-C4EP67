from flask import *
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client['c4e']
kpop_collection = db['Kpop']

app = Flask(__name__)

@app.route('/')
def homepage(): 
  idols = kpop_collection.find({})
  return render_template('homepage.html', idols_data=idols)

@app.route('/me')
def my_info():
  return 'this is me'

app.run(debug=True, port=3000)