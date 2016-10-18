import sqlite3
import csv

name = 'supreme-dollop.db'

db = sqlite3.connect(name)
c = db.cursor()

statement = "SELECT id,name FROM students;"
c.execute(statement)

ids = c.fetchall()

for i in ids:
    id_number = i[0]
    print id_number
    statement = "SELECT mark FROM courses WHERE id=" + str(id_number) + ";"
    c.execute(statement)

    marks = c.fetchall()
    average = 0
    count = 0
    for m in marks:
        mark = m[0]
        average += float(mark)
        count += 1

    average = average / count

    print ("Student with name: " + i[1] + " and id: " + str(id_number) + " has an average of " + str(average))
