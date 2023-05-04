
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
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

ARK_DB = "arkDB"

# Connect to database based using environment variables
db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
)

# Setting MySQL cursor to execute statements
mycursor = db.cursor()

# Creating creature database if doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS " + ARK_DB)

# Selecting Ark database
db.database = ARK_DB

# Create armor table in database if doesn't exist
mycursor.execute("""CREATE TABLE IF NOT EXISTS `armor` 
(`id` INT NOT NULL AUTO_INCREMENT,`armortype` VARCHAR(255) NOT NULL,`unlock_level` VARCHAR(255) NULL,`armor_rating` INT NULL,`cold_protection` VARCHAR(255) NULL,`heat_protection` VARCHAR(255) NULL,
`weight` INT NULL,`durability` INT NULL,`found_in` VARCHAR(255) NULL,`ingredients` VARCHAR(255) NULL, `url` VARCHAR(255) NULL, PRIMARY KEY (`id`, `armortype`))""")

statementPrep = """
INSERT INTO armor (armortype, unlock_level, armor_rating, cold_protection, heat_protection, weight, durability, found_in, ingredients, url) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

values = []

# Make GET request to ARK Fandom
r = requests.get('https://ark.fandom.com/wiki/Armor')

# Parsing the HTML
doc = BeautifulSoup(r.content, 'html.parser')

armorData = []
armorDict = {}

armorTable = doc.find(['table'], class_='wikitable')
amorTableBody = armorTable.tbody
armorTableRows = amorTableBody.find_all('tr')

for armorRow in armorTableRows:

    armorData = armorRow.find_all('td')
    if len(armorData) == 0:
        continue
    else:
        armorLink = "https://ark.fandom.com" + armorRow.find('a').get('href')

        armorData = [ele.text.strip() for ele in armorData]
        # print(armorData)
        newArmor = (armorData[0], armorData[1], armorData[2], armorData[3], armorData[4], armorData[5], armorData[6], armorData[7], armorData[8], armorLink)
        # print(newArmor)
        values.append(newArmor)

        armorDict[armorData[0]] = {
            "unlock_level": armorData[1], 
            "armor_rating": armorData[2], 
            "cold_protection": armorData[3],
            "heat_protection": armorData[4],
            "weight": armorData[5],
            "durability": armorData[6],
            "found_in": armorData[7],
            "ingredients": armorData[8],
            "url": armorLink
        }

mycursor.executemany(statementPrep, values)

db.commit()

print(mycursor.rowcount, "was inserted.")

with open('data.json', 'w') as fp:
    json.dump(armorDict, fp, indent=4)

