import mysql.connector

try:
    connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="TEJA",
    database="comm_6"


    )

    cursor = connection.cursor()


    Query= """INSERT INTO employees(
    employee_id,
    first_name,
    last_name,
    gender,
    department,
    designation,
    salary,
    hire_date,
    email,
    phone,
    city,
    state
    )
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

    """

    employees_data =[

    (52,"sam","Kumar","Male","CSC","Tester",25000,"2025-05-01","sam@gmail.com","9876543201","HYB","TG")
    ]

    cursor.executemany(Query, employees_data)   


    connection.commit()

    print("emp in successfully")

except mysql.connector.Error as error:

    print("Error",error)


finally:

    if "cursor" in locals ():
        cursor.close()

    if "connection" in locals () and connection.is_connected():
        connection.close()



