import sqlite3

connection = sqlite3.connect("dallas-ois.sqlite")

cur = connection.cursor()
result = cur.execute('''SELECT * FROM incidents WHERE case_number=( SELECT case_number FROM subjects WHERE full_name = "Curry, James")''').fetchall()

for line in result:
    print(line)
connection.close()

