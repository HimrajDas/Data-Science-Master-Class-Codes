import pymongo

client = pymongo.MongoClient("mongodb+srv://Himraj:My$MongodB$@cluster0.prceeb8.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# print(client)

db = client["TestingMongoDB"]    # This is Database name
create_collection = db["my_record"]     # This is collection

data = {
    "name": "Himraj",
    "learning": "Data Science",
    "timing": "felxi"
}

data1 = {
    "email": "IDK@gmail.com",
    "ph no": 8828183494
}

create_collection.insert_one(data)
create_collection.insert_one(data1)


data2 = {
    "course_list": ["Data Science", "Web Dev", "Java With DSA"],
    "mentor": ["sudhanshu", "anurag", "hyder"]
}

create_collection.insert_one(data2)

data3 = [
    { "name": "Amy", "address": "Apple st 652" },
    { "name": "Hannah", "address": "Mountain 21" },
    { "name": "Michael", "address": "Valley 345" },
    { "name": "Sandy", "address": "Ocean blvd 2" },
    { "name": "Betty", "address": "Green Grass 1" },
    { "name": "Richard", "address": "Sky st 331" },
    { "name": "Susan", "address": "One way 98" },
    { "name": "Vicky", "address": "Yellow Garden 2" },
    { "name": "Ben", "address": "Park Lane 38" },
    {"name": "William", "address": "Central st 954" },
    { "name": "Chuck", "address": "Main Road 989" },
    { "name": "Viola", "address": "Sideway 1633" }
]


create_collection.insert_many(data3)

data4 = {
 "name": "notebook",
 "qty": 50,
 "rating": [ { "score": 8 }, { "score": 9 } ],
 "size": { "height": 11, "width": 8.5, "unit": "in" },
 "status": "A",
 "tags": [ "college-ruled", "perforated"]
}

create_collection.insert_one(data4)

for i in create_collection.find():
    print(i)


list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},
    
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},
    
    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

create_collection.insert_many(list_of_records)



random_data = [
    {'_id': '3', 'companyName': 'iNeuron', 'Faculty': 'XYZ'},
    {'_id': '4', 'companyName': 'iNeuron', 'Faculty': 'ABC'},
    {'_id': '5', 'companyName': 'iNeuron', 'Faculty': 'PQR'},
]

create_collection.insert_many(random_data)

for i in create_collection.find({"companyName": "iNeuron"}):
    print(i)

for i in create_collection.find({"_id":{"$gte": "4"}}):     # "$gte" --> greater then equal, "$gt" --> greater than
    print(i)


create_collection.update_many({"companyName": "iNeuron"}, {"$set": {"companyName": "pwskills"}})

create_collection.drop()   # It will delete the collection