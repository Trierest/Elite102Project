import mysql.connector 

connection = mysql.connector.connect(
    user = 'python_connection',
    database = 'example1',
    password = '12345678!'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM weapons")
cursor.execute(testQuery)

addQuery = ("INSERT INTO weapons (name, damage, gem_price) VALUES ('Hat',1,40)")
# addData = ("INSERT INTO weapons (name, damage, gem_price) VALUES (\"Boots,7,7)")
cursor.execute(addQuery)
connection.commit()

for item in cursor:
    print(item)

cursor.close()
connection.close()
