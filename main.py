#print("Hello World!")
#Greeting menu for database
#theme: Banking
#
import mysql.connector 
# import unittest

connection = mysql.connector.connect(
    user = 'python_connection',
    database = 'example1',
    password = '12345678!'
)
cursor = connection.cursor()

# def account_exists(name):
    # cursor.execute("SELECT Name FROM banking WHERE EXISTS (SELECT Name FROM banking WHERE Name <=> '{name}')");
    # return cursor.execute(f"SELECT Name FROM banking WHERE Name <=> '{name}';")

# class TestInputs(unittest.TestCase):
#     def test_account_exists(self):  
#         self.assertTrue(account_exists("Robby"))
#         self.assertFalse(account_exists("Tri"))


# if __name__ == '__main__':
#     unittest.main()

print("Welcome to the Banking With B.")
# cursor.execute("SELECT Name FROM banking WHERE EXISTS (SELECT Name FROM banking WHERE Name <=> 'Tri')")


while True:
    print("-Select-")
    print("1. Add Account")
    print("2. Remove Account")
    print("3. Check Balance")
    print("4. Deposit Amount")
    print("5. Withdraw Amount")
    print("6. Edit Account")
    print("7. List Accounts")
    print("8. Exit and Save")
    
    menu_choice = input("> ")
    if menu_choice == "1":
        new_name = input("Enter Account Name: ")
        new_pin = input("Enter Account PIN: ")
        
        add_account = (f"INSERT INTO banking (Name, PIN, Balance) VALUES ('{new_name}', {new_pin}, 0)")
        cursor.execute(add_account)
        

    elif menu_choice == "2":
        delete = input("Choose the name of the account you want removed: ")
        delete_account = (f"DELETE FROM banking WHERE Name <=> '{delete}';")
        cursor.execute(delete_account)
        

    elif menu_choice == "3":
        account_check = input("Enter the Account name: ")
        select_account = (f"SELECT Balance FROM banking WHERE Name <=> '{account_check}';")
        cursor.execute(select_account)
        for item in cursor:
            print(item)
        
    elif menu_choice == "4":
        choose_account = input("Select account to add money to: ")
        choose_amount = int(input("Enter amount to add: $"));
        add_money = (f"UPDATE banking SET Balance = Balance + {choose_amount} WHERE Name <=> '{choose_account}';")
        cursor.execute(add_money)

    elif menu_choice == "5":
        choose_account = input("Select account to remove money from: ")
        take_amount = int(input("Enter amount to take out: $"));
        remove_money = (f"UPDATE banking SET Balance = Balance - {take_amount} WHERE Name <=> '{choose_account}';")
        cursor.execute(remove_money)

    elif menu_choice == "6":
        choose_account = input("Select account to change name from: ")
        choose_new_name = input("Enter new name: ")
        set_name = (f"UPDATE banking SET Name = '{choose_new_name}' WHERE Name <=> '{choose_account}'")
        cursor.execute(set_name)

    elif menu_choice == "7":
        list_accounts = ("SELECT * FROM banking;")
        cursor.execute(list_accounts)
        for accounts in cursor:
            print(accounts)

    elif menu_choice == "8":
        connection.commit()
        break

print("> Exitting the Database. Goodbye!")
cursor.close()
connection.close()