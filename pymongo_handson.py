from pymongo import MongoClient


# MongoDB hierarchy:
# - cluster/instance --> db --> collection --> document/post(dictionary) --> key --> value
# cluster = MongoClient('mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.dx4yh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
cluster = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
db = cluster["first-test"]
collection = db["users"]

# _id:
# - Each document/post is uniquely identified by _id.
# - If you don't specify _id, MongoDB will generate a unique random value for _id.
# - Ex: _id: ObjectId("60f158b76e5d66174224b9aa")
# - Without _id
post = {"name": "tim", "age": 27, "email": "tim@gmail.com"}
# - With _id
post0 = {"_id": 0, "name": "cook", "age": 35, "email": "cook@gmail.com"}
post1 = {"_id": 1, "name": "ram", "age": 35, "email": "ram@yahoo.com"}
post2 = {"_id": 2, "name": "sham", "age": 46, "email": "sham@gmail.com"}
post3 = {"_id": 3, "name": "bob", "age": 46, "email": "bob@yahoo.com"}

print('Insertion:')
print('- Inserting one document/post at a time.')
insert_one_result = collection.insert_one(post)
print('inserted_id: {}'.format(insert_one_result.inserted_id))
insert_one_result = collection.insert_one(post0)
print('inserted_id: {}'.format(insert_one_result.inserted_id))
print('- Inserting multiple documents/posts at a time.')
insert_many_result = collection.insert_many([post1, post2, post3])
print('inserted_ids: {}'.format(insert_many_result.inserted_ids))

print('Searching:')
print('- Search for documents in a collection by single field.')
# - .find()
cursor = collection.find({"age": 35})
# - .find() returns a cursor.
# - Cursor is a MongoDB Collection of the documents which is returned upon the find method execution.
print(cursor)
for document in cursor:
    print(document)
    for key, value in document.items():
        print('{} : {}'.format(key, value))
print('- Search for documents in a collection by multiple field.')
# - .find_one()
document = collection.find_one({"age": 35, "name": "ram"})
print(document)
print('- Search for documents in a collection using regex.')
# - .find()
cursor = collection.find({"email": {'$regex': 'gmail.com$'}})
print(cursor)
for document in cursor:
    print(document)
    for key, value in document.items():
        print('{} : {}'.format(key, value))
print('- Search for all documents in a collection.')
# cursor = collection.find({})
cursor = collection.find()
print(cursor)
for document in cursor:
    print(document)
    for key, value in document.items():
        print('{} : {}'.format(key, value))

print('Count: ')
print('- Number of documents with age=35')
count = collection.count_documents({'age': 35})
print(count)
print('- Total number of documents')
# count = collection.count_documents()
count = collection.count_documents({})
print(count)

print('Updation: - Using MongoDB update operators')
print('- Update one document')
update_result = collection.update_one({'_id': 3}, {'$set': {'name': 'alice', 'email': 'alice@gmail.com'}})
print('matched_count: {}'.format(update_result.matched_count))
print('modified_count: {}'.format(update_result.modified_count))
print('- Update multiple documents')
update_result = collection.update_many({'email': {'$regex': 'com$'}}, {
    '$set': {'address': 'Bengaluru'},
    "$inc": {'age': 5}
})
print('matched_count: {}'.format(update_result.matched_count))
print('modified_count: {}'.format(update_result.modified_count))

print('Deletion: ')
print('- Delete one document')
delete_result = collection.delete_one({"age": 51})
print('deleted_count: {}'.format(delete_result.deleted_count))
print('- Delete multiple documents')
delete_result = collection.delete_many({"age": 40})
print('deleted_count: {}'.format(delete_result.deleted_count))
print('- Delete all documents')
delete_result = collection.delete_many({})
print('deleted_count: {}'.format(delete_result.deleted_count))
