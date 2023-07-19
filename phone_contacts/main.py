import sqlite3
from sqlite3 import Error
import sys

conn = sqlite3.connect("./phone_contacts/main.db")

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_contact(conn, contact):
    sql = ''' INSERT INTO contacts(phone_number,first_name,last_name,addr,email_addr)
                VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"./phone_contacts/main.db"

    sql_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                    [contact_id] INTEGER PRIMARY KEY UNIQUE,
                                    [phone_number] NVARCHAR(10) NOT NULL UNIQUE,
                                    [first_name] NVARCHAR(50) NOT NULL,
                                    [last_name] NVARCHAR(50) NULL,
                                    [addr] NVARCHAR(255) NULL,
                                    [email_addr] NVARCHAR(255) NULL
                                );"""
    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_contacts_table)
    else:
        print("Error! cannot create the database connection.")

def add_contact():
    valid = False
    print()
    while not valid:
        phone_number = input("Please enter in a valid phone number.\n> ")
        c = conn.cursor()
        c.execute('''SELECT * FROM contacts WHERE phone_number = ?''', phone_number)
        check = c.fetchall()
        if len(check) == 0:
            valid = True
        else:
            print("\nYou already have this number saved in your contacts.")
    first_name = input("Please enter in the first name.\n> ")
    last_name = input("Please enter in the last name.\n> ")
    addr = input("Please enter in the full address.\n> ")
    email_addr = input("Please enter in the email address.\n> ")
    print()

    with conn:
        try:
            new_contact = (phone_number, first_name, last_name, addr, email_addr)
            create_contact(conn, new_contact)
        except Error:
            print("Please enter a unique phone number!")

def view_contacts():
    contact_query = '''SELECT * from contacts'''
    c = conn.cursor()
    c.execute(contact_query)
    records = c.fetchall()

    print()
    print(f"YOU CURRENTLY HAVE {len(records)} CONTACTS SAVED.\n")

    for row in records:
        print("Phone Number:", row[1])
        print("First Name:", row[2])
        print("Last Name:", row[3])
        print("Address:", row[4])
        print("Email Address:", row[5])
        print("\n")

    c.close()

INTRO = """(´• ω •`) ♡ WELCOME TO YOUR PHONE CONTACTS! (´ε｀ )♡
Type 'add' to add a new contact.
Type 'edit' to edit a contact.
Type 'view' to view your contacts.
Type 'delete' to delete a contact.
Type 'quit' to quit the program.
"""

if __name__ == "__main__":
    print(INTRO)
    main()

    user_choice = ""
    
    while user_choice != "quit":
        user_choice = input("Please select an option (add/edit/view/quit).\n> ")
        if user_choice == "add":
            add_contact()
        elif user_choice == "edit":
            print("Edit\n")
        elif user_choice == "delete":
            print("Delete\n")
        elif user_choice == "view":
            view_contacts()
    sys.exit()
