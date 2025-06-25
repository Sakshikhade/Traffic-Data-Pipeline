import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="myPass@1234",  # Replace this
        database="retail_personalization"     # Replace if your DB name is different
    )

    if connection.is_connected():
        print("Connection to MySQL database was successful!")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers;")
        rows = cursor.fetchall()

        print("Customer Data:")
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
