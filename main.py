#print("Hello World!")
#Greeting menu for database
#theme: database on items in video games (weapons)
import mysql.connector 

connection = mysql.connector.connect(
    user = 'python_connection',
    database = 'example1',
    password = '12345678!'
)

print("Welcome to the Weapon Arsenal.")
cursor = connection.cursor()

while True:
    print("-Select-")
    print("1. Add Weapon")
    print("2. Remove Weapon")
    print("3. List Items")
    print("4. Exit")
    
    menu_choice = input("> ")
    if menu_choice == "1":
        new_name = input("Enter weapon name: ")
        new_damage = input("Enter weapon damage: ")
        new_gem_price = input("Enter gem price: ")

        
        add_weapon = (f"INSERT INTO weapons (name, damage, gem_price) VALUES ('{new_name}', {new_damage}, {new_gem_price})")
        cursor.execute(add_weapon)
        connection.commit()

    elif menu_choice == "2":
        delete = input("Choose the name of the weapon you want removed: ")
        delete_weapon = (f"DELETE FROM weapons WHERE idWeapons <=> '{delete}';")
        cursor.execute(delete_weapon)
        connection.commit()

    elif menu_choice == "3":

        testQuery = ("SELECT * FROM weapons")
        cursor.execute(testQuery)

        for item in cursor:
            print(item)

    elif menu_choice == "4":
        break

print("> Exitting the arsenal. Goodbye!")
cursor.close()
connection.close()