import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=''
    )
    myer = conn.cursor()
    myer.execute("CREATE DATABASE STORM2")
except mysql.connector.Error as r:
    print(r)
    
print("done!")
 