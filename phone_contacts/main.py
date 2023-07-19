"""Phone Contacts

This program simulates a phone contacts app, allowing the user to add a new
contact, edit an existing contact, view all contacts, or delete a contact.
"""

import sqlite3
from sqlite3 import Error
import sys

DATABASE = r"./phone_contacts/main.db"

def create_connection(db_file):
    """returns a connection object to database file to interact with sqlite"""

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as err:
        print(err)
    return conn

def create_table(conn, create_table_sql):
    """creates contacts table if one does not already exist"""
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as err:
        print(err)

def add_contact(conn, contact):
    """adds the new contact to the contacts table"""
    sql = ''' INSERT INTO contacts(phone_number,first_name,last_name,addr,email_addr)
                VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid

def create_contact():
    """creates a new valid contact from user input"""
    conn = create_connection(DATABASE)
    valid = False
    print()
    while not valid:
        phone_number = input("Please enter in a valid phone number.\n> ")
        curr = conn.cursor()
        curr.execute('''SELECT * FROM contacts WHERE phone_number = ?''', phone_number)
        check = curr.fetchall()
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
            add_contact(conn, new_contact)
        except Error:
            print("Please enter a unique phone number!")
    conn.close()

def view_contacts():
    """print all contacts stored in contacts database"""
    conn = create_connection(DATABASE)
    contact_query = '''SELECT * from contacts'''
    curr = conn.cursor()
    curr.execute(contact_query)
    records = curr.fetchall()

    print()
    print(f"YOU CURRENTLY HAVE {len(records)} CONTACTS SAVED.\n")

    for row in records:
        print("Phone Number:", row[1])
        print("First Name:", row[2])
        print("Last Name:", row[3])
        print("Address:", row[4])
        print("Email Address:", row[5])
        print("\n")
    conn.close()

def main():
    """initial set up for contacts database"""
    sql_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                    [contact_id] INTEGER PRIMARY KEY UNIQUE,
                                    [phone_number] NVARCHAR(10) NOT NULL UNIQUE,
                                    [first_name] NVARCHAR(50) NOT NULL,
                                    [last_name] NVARCHAR(50) NULL,
                                    [addr] NVARCHAR(255) NULL,
                                    [email_addr] NVARCHAR(255) NULL
                                );"""

    conn = create_connection(DATABASE)

    if conn is not None:
        create_table(conn, sql_create_contacts_table)
    else:
        print("Error! cannot create the database connection.")
    conn.close()

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

    CHOICE = ""
    while CHOICE != "quit":
        CHOICE = input("Please select an option (add/edit/view/quit).\n> ")
        if CHOICE == "add":
            create_contact()
        elif CHOICE == "edit":
            print("Edit\n")
        elif CHOICE == "delete":
            print("Delete\n")
        elif CHOICE == "view":
            view_contacts()

    sys.exit()
