import mysql.connector

conn = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="employee_management"

)

cursor = conn.cursor()