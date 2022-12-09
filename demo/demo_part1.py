import csv
from pymongo import MongoClient

'''
CONNECTING TO THE MONGO SERVER
Requires the user and password
Points to where the data is stored
'''
mongoClient = MongoClient('mongodb+srv://admin:3223@cluster0.ikidhhk.mongodb.net/eBIRD')

db = mongoClient.eBIRD
data = db.ColumbiaFull

'''
GETTING THE BIRD OF INTEREST
Gets an input from the user and uses the list of known birds to ensure the user types the correct bird
'''
birds = ["Bananaquit","Bicolored Wren","Black Vulture","Black-chested Jay","Blue-gray Tanager","Brown Pelican","Brown-throated Parakeet",
"Cattle Egret","Cattle Tyrant","Great Kiskadee","House Wren","Palm Tanager","Roadside Hawk","Ruddy Ground Dove","Smooth-billed Ani",
"Southern Lapwing","Tropical Kingbird","Turkey Vulture","Yellow-bellied Elaenia","Yellow-headed Caracara"]

print("Please type the name of the bird you want to know more about from the options below: \t")
for bird in birds:
    print(bird)

choice = input(">>> ")

#ensuring that the bird chosen is one of the ones in the database
while(choice not in birds):
    print("\nThat bird is not one of the options. Give the name exactly as seen.\n")
    print("Please type the name of the bird you want to know more about from the options below: \t")
    for bird in birds:
        print(bird)

    choice = input(">>> ")

'''
PERFORMING THE QUERYING AND FILTERING OF THE DATA
'''
print("Searching for " +choice)
#query and filter
cursor = data.find({"COMMON NAME":choice},{"COMMON NAME":1,"LATITUDE":1,"LONGITUDE":1,"OBSERVATION DATE":1})

'''
OUTPUTTING RESULTS TO A CSV FILE
'''
csv_file = choice+".csv"
csv_columns  = ['_id', 'COMMON NAME','LATITUDE', 'LONGITUDE','OBSERVATION DATE']

listOfDicts = []

for doc in cursor:
    listOfDicts.append(doc)

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
    writer.writeheader()
    writer.writerows(listOfDicts)

print("Writing to csv")

#tracking what bird is chosen to use in demo_part3.py
with open('chosen_bird.txt','w') as f:
    print(choice, file = f)