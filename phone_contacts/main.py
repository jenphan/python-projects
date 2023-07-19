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
    sql = ''' INSERT INTO contacts(first_name,last_name,addr_id,phone_number,email_addr)
                VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"./phone_contacts/main.db"

    sql_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                    [contact_id] INTEGER PRIMARY KEY,
                                    [first_name] NVARCHAR(50) NOT NULL,
                                    [last_name] NVARCHAR(50) NULL,
                                    [addr_id] INTEGER NOT NULL,
                                    [phone_number] NVARCHAR(255) NOT NULL,
                                    [email_addr] NVARCHAR(255) NOT NULL,
                                    FOREIGN KEY(addr_id) REFERENCES contacts(addr_id)
                                );"""
    
    sql_create_address_table = """ CREATE TABLE IF NOT EXISTS address (
                                    [addr_id] INTEGER PRIMARY KEY,
                                    [addr] NVARCHAR(255) NULL,
                                    [addr2] NVARCHAR(255) NULL,
                                    [city] NVARCHAR(255) NULL,
                                    [state] NVARCHAR(255) NULL,
                                    [zipcode] NVARCHAR(5)
                                )
                                """
    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_contacts_table)
        create_table(conn, sql_create_address_table)
    else:
        print("Error! cannot create the database connection.")
    
    with conn:
        addr = ('ADDRESS 1', 'ADDRESS 2' , 'CITY', 'STATE', 'ZIPCODE')
        addr_id = create_addr(conn, addr)

        new_contact = ('FIRST NAME', 'LAST NAME', addr_id, 'PHONE NUMBER', 'EMAIL ADDRESS')
        create_contact(conn, new_contact)

if __name__ == "__main__":
    main()