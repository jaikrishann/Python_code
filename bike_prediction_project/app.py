# # #django
# # #flask
# # #streamlit
# # #fast api
# # #rest api
# # #front end --> html/css
# # #backend --> python flask is a web framework 


# # from flask import Flask , render_template, url_for, request
# # import joblib

# # import pandas as pd 

# # # import mysql.connector

# # # Connect to the database
# # # conn = mysql.connector.connect(
# # #     host="localhost",
# # #     user="root",
# # #     password="1234",
# # #     database=" "

# # # )
# # # if conn.is_connected():
# # #     print("connection is established ")
# # # else:
# # #     print("not conn")    

# # # mysql_cursor = conn.cursor()
# # # query = "INSERT INTO bike_predictions (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction) VALUES (%s, %s, %s, %s, %s, %s)"

# # model = joblib.load('RD_model.lb')
# # app = Flask(__name__)


# # @app.route('/')                    # (/) --> home route 
# # def home():
# #     return render_template('index.html')

# # @app.route('/project')
# # def project():
# #     return render_template('project.html')

# # @app.route('/about')
# # def about():
# #     return render_template('about.html')

# # @app.route('/contact')
# # def contactus():
# #     return render_template('contact.html')

# # # @app.route('/history')
# # # def history():
# # #     # Create a cursor object
# # #     # mysql_cursor = conn.cursor()                 #dictionary=True
# # #     conn = mysql.connector.connect(
# # #     host="localhost",
# # #     user="root",
# # #     password="1234",
# # #     database="bike_predicted_data"

# # #     )   
# # #     mysql_cursor = conn.cursor()
# # #     query = "INSERT INTO bike_predictions (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction) VALUES (%s, %s, %s, %s, %s, %s)"


# # #     try:
# # #         # Execute the SELECT query to fetch historical data
# # #         query = "SELECT * FROM bike_predictions"
# # #         mysql_cursor.execute(query)

# # #         # Fetch all the results
# # #         historical_data = mysql_cursor.fetchall()

# # #     except mysql.connector.Error as error:
# # #         print("Error:", error)
# # #         historical_data = []
# # #         print('hiiiiiiiiii')

# # #     finally:
# # #         pass
# # #         # # Close the cursor
# # #         mysql_cursor.close()
# # #         conn.close()

# # #     # Pass the historical data to the history.html template for rendering
# # #     return render_template("history.html", historical_data=historical_data)



# # @app.route('/predict',methods=['GET','POST'])
# # def predict():
# #     if request.method=='POST':
# #         brand_name = request.form['brand_name']
# #         owner_name=int(request.form['owner'])
# #         age_bike=int(request.form['age'])
# #         power_bike= int(request.form['power'])
# #         kms_driven_bike= int(request.form['kms_driven'])
# #         bike_numbers={'TVS': 0,
# #                         'Royal Enfield': 1,
# #                         'Triumph': 2,
# #                         'Yamaha': 3,
# #                         'Honda': 4,
# #                         'Hero': 5,
# #                         'Bajaj': 6,
# #                         'Suzuki': 7,
# #                         'Benelli': 8,
# #                         'KTM': 9,
# #                         'Mahindra': 10,
# #                         'Kawasaki': 11,
# #                         'Ducati': 12,
# #                         'Hyosung': 13,
# #                         'Harley': 14,
# #                         'Jawa': 15,
# #                         'BMW': 16,
# #                         'Indian': 17,
# #                         'Rajdoot': 18,
# #                         'LML': 19,
# #                         'Yezdi': 20,
# #                         'MV': 21,
# #                         'Ideal': 22}
        
# #         brand_name_encode=bike_numbers[brand_name]
# #         lst=[[owner_name,brand_name_encode,kms_driven_bike,age_bike,power_bike]]  #sequence order
# #         pred = model.predict(lst)
# #         pred = pred[0]
# #         pred = round(pred, 2)
# #         user_data = (str(owner_name),str(brand_name),kms_driven_bike,age_bike,power_bike,pred)


# #     #     try:
# #     # # Execute the query with user data
# #     #         mysql_cursor.execute(query, user_data)
# #     #         print("row is instered :", mysql_cursor.rowcount)
    
# #     # Commit the transaction
# #     #         conn.commit()

# #     #     except mysql.connector.Error as error:
# #     #         print("Error:", error)

# #     #     finally:
# #     # # Close the cursor and connection
# #     #         mysql_cursor.close()
# #     #         conn.close()
# #         return render_template("project.html",prediction=str(pred))
    



    
   


# # if __name__ == "__main__":
# #     app.run(host='0.0.0.0',port=2525,debug=True)




# # #  mysql_cursor = conn.cursor(dictionary=True)

# # #     try:
# # #         # Execute the SELECT query to fetch historical data
# # #         query = "SELECT * FROM bike_predictions"
# # #         mysql_cursor.execute(query)

# # #         # Fetch all the results
# # #         historical_data = mysql_cursor.fetchall()

# # #     except mysql.connector.Error as error:
# # #         print("Error:", error)
# # #         historical_data = []

# # #     finally:
# # #         # Close the cursor
# # #         mysql_cursor.close()

# # #     # Pass the historical data to the history.html template for rendering
# # #     return render_template("history.html", historical_data=historical_data)
# # # form tag laga le user se brand name ka input leke phir history uss brand name ke according show karna hai aur ussko aur presentable banana hai 


# from flask import Flask, render_template, request
# import joblib
# import mysql.connector
# import pandas as pd

# # Load the prediction model
# model = joblib.load('RD_model.lb')

# # Initialize the Flask app
# app = Flask(__name__)

# # MySQL database connection function
# def get_db_connection():
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="1234",
#             database="bike_predicted_data"
#         )
#         return conn
#     except mysql.connector.Error as error:
#         print("Error connecting to MySQL:", error)
#         return None

# # Routes
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/project')
# def project():
#     return render_template('project.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contactus():
#     return render_template('contact.html')

# # History route with optional brand filter
# @app.route('/history', methods=['GET', 'POST'])
# def history():
#     brand_name_filter = request.form.get('brand_name_filter', None)
#     conn = get_db_connection()
#     historical_data = []

#     if conn:
#         cursor = conn.cursor(dictionary=True)
#         try:
#             # If brand_name_filter is provided, filter by brand name
#             if brand_name_filter:
#                 query = "SELECT * FROM bike_predictions WHERE brand_name = %s"
#                 cursor.execute(query, (brand_name_filter,))
#             else:
#                 query = "SELECT * FROM bike_predictions"
#                 cursor.execute(query)

#             # Fetch all historical data
#             historical_data = cursor.fetchall()
#         except mysql.connector.Error as error:
#             print("Error fetching historical data:", error)
#         finally:
#             cursor.close()
#             conn.close()

#     return render_template("history.html", historical_data=historical_data)

# # Prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         try:
#             # Get form data
#             brand_name = request.form['brand_name']
#             owner_name = int(request.form['owner'])
#             age_bike = int(request.form['age'])
#             power_bike = int(request.form['power'])
#             kms_driven_bike = int(request.form['kms_driven'])

#             # Encode brand name
#             bike_numbers = {
#                 'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3,
#                 'Honda': 4, 'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8,
#                 'KTM': 9, 'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12,
#                 'Hyosung': 13, 'Harley': 14, 'Jawa': 15, 'BMW': 16,
#                 'Indian': 17, 'Rajdoot': 18, 'LML': 19, 'Yezdi': 20,
#                 'MV': 21, 'Ideal': 22
#             }
#             brand_name_encode = bike_numbers.get(brand_name, -1)

#             # Make prediction
#             input_data = [[owner_name, brand_name_encode, kms_driven_bike, age_bike, power_bike]]
#             pred = model.predict(input_data)[0]
#             prediction = round(pred, 2)

#             # Save prediction to the database
#             conn = get_db_connection()
#             if conn:
#                 cursor = conn.cursor()
#                 query = "INSERT INTO bike_predictions (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction) VALUES (%s, %s, %s, %s, %s, %s)"
#                 user_data = (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction)
#                 cursor.execute(query, user_data)
#                 conn.commit()
#                 cursor.close()
#                 conn.close()

#             return render_template("project.html", prediction=str(prediction))

#         except Exception as e:
#             print("Error in prediction:", e)
#             return render_template("project.html", prediction="An error occurred.")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=2525, debug=True)

from flask import Flask, render_template, request
import joblib
import sqlite3
import pandas as pd

# Load the prediction model
model = joblib.load('RD_model.lb')

# Initialize the Flask app
app = Flask(__name__)

# SQLite database connection function
def get_db_connection():
    try:
        conn = sqlite3.connect('bike_predicted_data.db')
        conn.row_factory = sqlite3.Row  # Enables dictionary-like access
        return conn
    except sqlite3.Error as error:
        print("Error connecting to SQLite:", error)
        return None

# Create table if not exists
def initialize_database():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bike_predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_name INTEGER,
                brand_name TEXT,
                kms_driven_bike INTEGER,
                age_bike INTEGER,
                power_bike INTEGER,
                prediction REAL
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()

# Initialize database on startup
initialize_database()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactus():
    return render_template('contact.html')

# History route with optional brand filter
@app.route('/history', methods=['GET', 'POST'])
def history():
    brand_name_filter = request.form.get('brand_name_filter', None)
    conn = get_db_connection()
    historical_data = []

    if conn:
        cursor = conn.cursor()
        try:
            if brand_name_filter:
                query = "SELECT * FROM bike_predictions WHERE brand_name = ?"
                cursor.execute(query, (brand_name_filter,))
            else:
                query = "SELECT * FROM bike_predictions"
                cursor.execute(query)

            historical_data = [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as error:
            print("Error fetching historical data:", error)
        finally:
            cursor.close()
            conn.close()

    return render_template("history.html", historical_data=historical_data)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data
            brand_name = request.form['brand_name']
            owner_name = int(request.form['owner'])
            age_bike = int(request.form['age'])
            power_bike = int(request.form['power'])
            kms_driven_bike = int(request.form['kms_driven'])

            # Encode brand name
            bike_numbers = {
                'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3,
                'Honda': 4, 'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8,
                'KTM': 9, 'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12,
                'Hyosung': 13, 'Harley': 14, 'Jawa': 15, 'BMW': 16,
                'Indian': 17, 'Rajdoot': 18, 'LML': 19, 'Yezdi': 20,
                'MV': 21, 'Ideal': 22
            }
            brand_name_encode = bike_numbers.get(brand_name, -1)

            # Make prediction
            input_data = [[owner_name, brand_name_encode, kms_driven_bike, age_bike, power_bike]]
            pred = model.predict(input_data)[0]
            prediction = round(pred, 2)

            # Save prediction to the SQLite database
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                query = '''INSERT INTO bike_predictions 
                    (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction) 
                    VALUES (?, ?, ?, ?, ?, ?)'''
                user_data = (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction)
                cursor.execute(query, user_data)
                conn.commit()
                cursor.close()
                conn.close()

            return render_template("project.html", prediction=str(prediction))

        except Exception as e:
            print("Error in prediction:", e)
            return render_template("project.html", prediction="An error occurred.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2525, debug=True)
