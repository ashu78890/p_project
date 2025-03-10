import mysql.connector

db = mysql.connector.connect(
    host="localhost",   
    user="root",        
    password="root",  
    database="testdb"   
)


if db.is_connected():
    print("Connected to MySQL successfully!")

cursor = db.cursor()

# sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
# values = ("Laptop", 75000.00, 5)

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for item in users:
    print(item,"values printed")


# db.commit() 

print("Product inserted successfully!")

# Close connection
cursor.close()
db.close()
