from pymongo import MongoClient
import csv

mongoClient = MongoClient('mongodb+srv://admin:3223@cluster0.ikidhhk.mongodb.net/eBIRD')

db = mongoClient.eBIRD
data = db.ColumbiaFull

birds = ["Bananaquit",
"Bicolored Wren",
"Black Vulture",
"Black-chested Jay",
"Blue-gray Tanager",
"Brown Pelican",
"Brown-throated Parakeet",
"Cattle Egret",
"Cattle Tyrant",
"Great Kiskadee",
"House Wren",
"Palm Tanager",
"Roadside Hawk",
"Ruddy Ground Dove",
"Smooth-billed Ani",
"Southern Lapwing",
"Tropical Kingbird",
"Turkey Vulture",
"Yellow-bellied Elaenia",
"Yellow-headed Caracara",]

for i in range(len(birds)):
    cursor = data.find({"COMMON NAME":birds[i]},{"COMMON NAME":1,"LATITUDE":1,"LONGITUDE":1,"OBSERVATION DATE":1})

    csv_file = birds[i]+".csv"
    csv_columns  = ['_id', 'COMMON NAME','LATITUDE', 'LONGITUDE','OBSERVATION DATE']

    listOfDicts = []

    for doc in cursor:
        listOfDicts.append(doc)

    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
        writer.writeheader()
        writer.writerows(listOfDicts)

