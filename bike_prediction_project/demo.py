import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    # database="bike_predicted_data"

)
if conn.is_connected():
    print("connection is established ")
else:
    print("not conn")  