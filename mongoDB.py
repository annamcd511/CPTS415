import csv
from pymongo import MongoClient

mongoClient = MongoClient('mongodb+srv://admin:3223@cluster0.ikidhhk.mongodb.net/eBIRD') 
db = mongoClient.eBIRD
db.Columbia.drop()

header = ["GLOBAL UNIQUE IDENTIFIER","LAST EDITED DATE","TAXONOMIC ORDER","CATEGORY","TAXON CONCEPT ID","COMMON NAME","SCIENTIFIC NAME","SUBSPECIES COMMON NAME","SUBSPECIES SCIENTIFIC NAME","EXOTIC CODE",
"OBSERVATION COUNT","BREEDING CODE","BREEDING CATEGORY","BEHAVIOR CODE","AGE/SEX","COUNTRY","COUNTRY CODE","STATE","STATE CODE","COUNTY","COUNTY CODE","IBA CODE","BCR CODE","USFWS CODE","ATLAS BLOCK",
"LOCALITY","LOCALITY ID","LOCALITY TYPE","LATITUDE","LONGITUDE","OBSERVATION DATE","TIME OBSERVATIONS STARTED","OBSERVER ID","SAMPLING EVENT IDENTIFIER","PROTOCOL TYPE","PROTOCOL CODE","PROJECT CODE",
"DURATION MINUTES","EFFORT DISTANCE KM","EFFORT AREA HA","NUMBER OBSERVERS","ALL SPECIES REPORTED","GROUP IDENTIFIER","HAS MEDIA","APPROVED","REVIEWED","REASON","TRIP COMMENTS","SPECIES COMMENTS"]
csvfile = open('ebd_CO_relAug-2022.txt', 'r', encoding="utf-8-sig")
reader = csv.DictReader( csvfile, delimiter='\t' )

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
        
    print (row)
    db.Columbia.insert_one(row)
