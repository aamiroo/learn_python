"""
We use SQL for database management.
"""
# Python's own library for SQL
import sqlite3     

# Creating a database file with the .db extension
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Creating database data with SQL commands
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (id INT PRIMARY KEY, name VARCHAR(50), age INT)               
""");

cursor.execute("""INSERT INTO student (id, name, age) VALUES (3, "ali", 21) ,(4,"hosein",22);""")

# Save changes
conn.commit()
cursor.execute("SELECT * FROM student")   # Reading data

for student in cursor.fetchall():
    print (student)

# Closing the connection to database
conn.close()