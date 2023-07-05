import psycopg2
import json
from color_decision import dic

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="pytest",
    user="pytest",
    password="pytest1",
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Convert the dictionary to a JSON string
json_str = json.dumps(dic)

# Define the SQL query to insert the JSON data into a table
query = "INSERT INTO pytest (json_data) VALUES (%s)"

# Execute the query with the JSON data as a parameter
cursor.execute(query, (json_str,))

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()
