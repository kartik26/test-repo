from random import seed
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int , username text, password text)"

cursor.execute(create_table)

user = (1,'kartik','asdf')

insert_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(insert_query,user)

user_list = [
    (2,'adarsh','hgsh'),
    (3,'anuj','huhdu')
]
cursor.executemany(insert_query,user_list)
select_query = "SELECT * FROM users"

for i in cursor.execute(select_query):
    print(i)

connection.commit()
connection.close()