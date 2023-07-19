import sqlite3
from sqlite3 import Error

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

def create_addr(conn, address):
    sql = ''' INSERT INTO address(addr,addr2,city,state,zipcode)
                VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, address)
    conn.commit()
    return cur.lastrowid

def create_contact(conn, contact):
    sql = ''' INSERT INTO contacts(phone_number,first_name,last_name,addr_id,email_addr)
                VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"./phone_contacts/main.db"

    sql_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                    [contact_id] INTEGER PRIMARY KEY,
                                    [phone_number] NVARCHAR(10) NOT NULL,
                                    [first_name] NVARCHAR(50) NOT NULL,
                                    [last_name] NVARCHAR(50) NULL,
                                    [addr_id] INTEGER NULL,
                                    [email_addr] NVARCHAR(255) NULL,
                                    FOREIGN KEY(addr_id) REFERENCES contacts(addr_id)
                                );"""
    
    sql_create_address_table = """ CREATE TABLE IF NOT EXISTS address (
                                    [addr_id] INTEGER PRIMARY KEY,
                                    [addr] NVARCHAR(100) NULL,
                                    [addr2] NVARCHAR(100) NULL,
                                    [city] NVARCHAR(60) NULL,
                                    [state] NVARCHAR(15) NULL,
                                    [zipcode] NVARCHAR(5) NULL
                                )
                                """
    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_contacts_table)
        create_table(conn, sql_create_address_table)
    else:
        print("Error! cannot create the database connection.")

def add_contact():
    phone_number = input("Please enter in the phone number (no dashes)\n> ")
    first_name = input("Please enter in the first name.\n> ")
    last_name = input("Please enter in the last name.\n> ")
    addr_1 = input("Please enter in the first address line.\n> ")
    addr_2 = input("Please enter in additional address information.\n> ")
    city = input("Please enter in the city.\n> ")
    state = input("Please enter in the state.\n> ")
    zipcode = input("Please enter in the zipcode.\n> ")
    email_addr = input("Please enter in the email address.\n> ")

    with conn:
        addr_id = create_addr(conn, (addr_1, addr_2 , city, state, zipcode))

        new_contact = (phone_number, first_name, last_name, addr_id, email_addr)
        create_contact(conn, new_contact)

if __name__ == "__main__":
    main()
    add_contact()