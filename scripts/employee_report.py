import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="tech_admin",
        password="1",
        database="techcorp"
        )

cursor = db.cursor()

cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(f"Employee ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Department: {row[2]}")
    print(f"Salary: R{row[3]}")
    print("-" * 20)


cursor.close()

db.close()


