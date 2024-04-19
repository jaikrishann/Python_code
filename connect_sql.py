import mysql.connector as mc

# Establishing connection with MySQL server on a cloud
# conn = mc.connect(
#     user="raj",
#     password="hello12345@",
#     host='52.66.212.209',
#     port=3306,
#     auth_plugin='mysql_native_password'
# )

# on a localhost 

conn = mc.connect(
    user="root",
    password="root12345@",
    host='localhost',
    port=3306,
    database='laptopdb'

)

if conn.is_connected():
    print('connected')
else:
    print('unable to connect')

mycur = conn.cursor()
query = "select * from table_name"



try:
    mycur.execute(query)
except:
    print('sorry we did,nt fetch records from database')
row = mycur.fetchall()
for i in row:
    print(i)
mycur.close()
conn.close()