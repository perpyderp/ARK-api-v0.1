
'''
This code was created by Jacob Cuison
Purpose is to scrape information from ARK Fandom and store into a MySQL Database and exposed using ARK Api
'''

import requests
import json
import mysql.connector
from bs4 import BeautifulSoup

import os
from dotenv import load_dotenv

# Loading environment files from .env
load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

CREATURE_DB = "creatureDB"

# Connect to database based using environment variables
db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
)

# Setting MySQL cursor to execute statements
mycursor = db.cursor()

# Creating creature database if doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS " + CREATURE_DB)

# Selecting creature database
db.database = CREATURE_DB

mycursor.execute("""CREATE TABLE IF NOT EXISTS `creatures` 
(`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(255) NOT NULL,`diet` VARCHAR(255) NULL,`temperament` VARCHAR(255) NULL,`tameable` VARCHAR(255) NULL,`rideable` VARCHAR(255) NULL,
`breedable` VARCHAR(255) NULL,`saddleLevelObtained` VARCHAR(255) NULL,`creatureID` VARCHAR(255) NULL,`url` VARCHAR(255) NULL, PRIMARY KEY (`id`, `name`))""")

statementPrep = """
INSERT INTO creatures (name, diet, temperament, tameable, rideable, breedable, saddleLevelObtained, creatureID, url) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

values = []

# Make GET request to ARK Fandom
r = requests.get('https://ark.fandom.com/wiki/Creatures')

# Parsing the HTML
doc = BeautifulSoup(r.content, 'html.parser')

creatureData = []
creatureDict = {}

creatureTable = doc.find(['table'], class_='cargo-creature-table')
creatureTableBody = creatureTable.tbody
creatureTableRows = creatureTableBody.find_all('tr')

for creatureRow in creatureTableRows:

    creatureData = creatureRow.find_all('td')
    if len(creatureData) == 0:
        continue
    else:
        creatureLink = "https://ark.fandom.com" + creatureRow.find('a').get('href')

        creatureData = [ele.text.strip() for ele in creatureData]

        newCreature = (creatureData[0], creatureData[2], creatureData[3], creatureData[4], creatureData[5], creatureData[6], creatureData[7], creatureData[8], creatureLink)

        values.append(newCreature)

        creatureDict[creatureData[0]] = {
            "diet": creatureData[2], 
            "temperament": creatureData[3], 
            "tameable": creatureData[4],
            "rideable": creatureData[5],
            "breedable": creatureData[6],
            "saddleLevelObtained": creatureData[7],
            "creatureID": creatureData[8],
            "url": creatureLink
        }

mycursor.executemany(statementPrep, values)

db.commit()

print(mycursor.rowcount, "was inserted.")

with open('data.json', 'w') as fp:
    json.dump(creatureDict, fp, indent=4)

