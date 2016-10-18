import sqlite3 
import csv

name = "supreme-dollop.db"

db = sqlite3.connect(name)
c = db.cursor()

statement = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(statement)

obj = open("peeps.csv")
d = csv.DictReader(obj)

for k in d:
    p = 'INSERT INTO students VALUES ("' + k['name'] +  '", "' + k['age'] +  '", "' + k['id'] + '" )'
    c.execute(p)
    
statement = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(statement)
obj = open("courses.csv")
d = csv.DictReader(obj)
for k in d:
    p = 'INSERT INTO courses VALUES ("' + k['code'] +  '", "' + k['id'] + '", "' + k['mark']  + '" )'
    c.execute(p)
    db.commit()
db.close()

                        
