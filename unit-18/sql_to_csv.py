
import csv 
import sqlite3

conn = sqlite3.connect('blogger.sqldb')
cursor = conn.cursor()

cursor.execute("SELECT * FROM post;")

with open('blogger.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in cursor.description])
    writer.writerows(cursor)

conn.close()
