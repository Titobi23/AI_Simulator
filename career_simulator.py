import mysql.connector
from mysql.connector import Error

# Function to create a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='career_simulator', 
            user='root',
            password='new_password'  
        )
        if connection.is_connected():
            print("Connection to MySQL database successful")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to get career paths from the database
def get_career_paths(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM career_paths;")
        result = cursor.fetchall()
        for row in result:
            print(f"Career ID: {row[0]}, Career Path: {row[1]}")
    except Error as e:
        print(f"Error while fetching data: {e}")

# Main function to run the program
def main():
    connection = create_connection()  
    if connection:  
        get_career_paths(connection)  
        connection.close()  
        print("MySQL connection closed")

if __name__ == "__main__":
    main()

