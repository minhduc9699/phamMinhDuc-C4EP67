import pymongo
from bson import ObjectId
from faker import Faker
faker = Faker()

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['c4e']
customer_collection = db['customer']


# create
new_data = []
for i in range(100):
  data = {
    'name': faker.name(),
    'address': faker.address(),
    'phone': faker.phone_number()
  }
  new_data.append(data)

customer_collection.insert_many(new_data)

# # READ
# # data = customer_collection.find({})
# data = customer_collection.find_one({'_id': ObjectId('5e55205602b909eb5ddb1c3a')})
# print(data)
# # for customer in data:
#   # print(customer)

# # update
# customer_collection.update_one(
#   {
#     '_id': ObjectId('5e55205602b909eb5ddb1c3a')
#   },
#   {
#     '$set': {
#       'name': 'Không phải Phượng'
#     }
#   }
# )

# # delete

# # customer_collection.delete_one({'_id': ObjectId('5e55205602b909eb5ddb1c3a')})