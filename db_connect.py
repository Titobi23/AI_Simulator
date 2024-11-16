import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='career_simulator',
        user='root',
        password='new_password'  
    )
    if connection.is_connected():
        print("Connection to MySQL database successful")
except Error as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")

def main():
    connection = create_connection()
    if connection:
        get_career_paths(connection)
        connection.close()
        print("MySQL connection closed")

if __name__ == "__main__":
    main()
