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
    query = '''INSERT INTO contacts(phone_number,first_name,last_name,addr,email_addr)
                VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(query, contact)
    conn.commit()
    return cur.lastrowid

def create_contact(conn):
    """creates a new valid contact from user input"""
    valid = False
    print()
    while not valid:
        phone_number = input("Please enter in a valid phone number.\n> ")
        cur = conn.cursor()
        try:
            cur.execute('''SELECT * FROM contacts WHERE phone_number = ?''', str(phone_number))
            check = cur.fetchall()
            if len(check) == 0:
                valid = True
            else:
                print("\nYou already have this number saved in your contacts.")
        except Error:
            if len(phone_number) <= 10:
                valid = True
    first_name = input("Please enter in the first name.\n> ")
    last_name = input("Please enter in the last name.\n> ")
    addr = input("Please enter in the full address.\n> ")
    email_addr = input("Please enter in the email address.\n> ")
    print()

    with conn:
        new_contact = (phone_number, first_name, last_name, addr, email_addr)
        add_contact(conn, new_contact)

def edit_contact(conn):
    """edit information from a specified, existing contact"""
    cur = conn.cursor()
    print("\nPlease enter in the phone number you would like to edit.")
    choice = input("> ")

    cur.execute("SELECT rowid FROM contacts WHERE phone_number = ?", (choice,))
    records = cur.fetchone()
    if records is None:
        print("This number is not currently saved as a contact.\n")
    else:
        print("\nPress 'enter' if you would not like to change the information.\n")
        first_name = input("Please enter in the first name.\n> ")
        if first_name != "":
            cur.execute("UPDATE contacts SET first_name = ?", first_name)
        last_name = input("Please enter in the last name.\n> ")
        if last_name != "":
            cur.execute("UPDATE contacts SET last_name = ?", last_name)
        addr = input("Please enter in the full address.\n> ")
        if addr != "":
            cur.execute("UPDATE contacts SET addr = ?", addr)
        email_addr = input("Please enter in the email address.\n> ")
        if email_addr != "":
            cur.execute("UPDATE contacts SET email_addr = ?", email_addr)
        print()

def view_contacts(conn):
    """print all contacts stored in contacts database"""
    query = '''SELECT * from contacts'''
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()

    print()
    print(f"YOU CURRENTLY HAVE {len(records)} CONTACTS SAVED.\n")

    for row in records:
        print("Phone Number:", row[1])
        print("First Name:", row[2])
        print("Last Name:", row[3])
        print("Address:", row[4])
        print("Email Address:", row[5])
        print("\n")

def delete_contact(conn):
    print("Delete")

def main():
    """initial set up for contacts database"""
    contacts = """ CREATE TABLE IF NOT EXISTS contacts (
                                    [contact_id] INTEGER PRIMARY KEY UNIQUE,
                                    [phone_number] NVARCHAR(10) NOT NULL UNIQUE,
                                    [first_name] NVARCHAR(50) NOT NULL,
                                    [last_name] NVARCHAR(50) NULL,
                                    [addr] NVARCHAR(255) NULL,
                                    [email_addr] NVARCHAR(255) NULL
                                );"""

    conn = create_connection(DATABASE)

    if conn is not None:
        create_table(conn, contacts)
        return conn
    else:
        print("Error! cannot create the database connection.")

INTRO = """(´• ω •`) ♡ WELCOME TO YOUR PHONE CONTACTS! (´ε｀ )♡
Type 'add' to add a new contact.
Type 'edit' to edit a contact.
Type 'view' to view your contacts.
Type 'delete' to delete a contact.
Type 'quit' to quit the program.
"""

if __name__ == "__main__":
    print(INTRO)
    CONN = main()

    CHOICE = ""
    while CHOICE != "quit":
        CHOICE = input("Please select an option (add/edit/view/delete/quit).\n> ")
        if CHOICE == "add":
            create_contact(CONN)
        elif CHOICE == "edit":
            edit_contact(CONN)
        elif CHOICE == "delete":
            delete_contact(CONN)
        elif CHOICE == "view":
            view_contacts(CONN)

    CONN.close()
    sys.exit()
