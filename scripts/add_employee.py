import mysql.connector

try: 
    db = mysql.connector.connect(
        host="localhost",
        user="tech_admin",
        password="1",
        database="techcorp"
        )

    cursor = db.cursor()
    name = input("Enter the name: ")
    lastName = input("Enter last name: ")
    department = input("Enter the department: ")
    salary = input("Enter the salary amount: ")

    sql = "INSERT INTO employees (first_name, last_name, department, salary) VALUES (%s, %s, %s, %s)"

    val = (name, lastName,  department, salary)



    cursor.execute(sql, val)
    db.commit()


    print(f"\nSuccess: {cursor.rowcount} employee added to the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()

