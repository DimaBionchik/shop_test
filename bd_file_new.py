import sqlite3 as sl

def create_tables(name_of_bd:str):
    connect = sl.connect(name_of_bd)
    with connect as con :
        con.execute("""
            CREATE TABLE IF NOT EXISTS Staff(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            login VARCHAR,
            password VARCHAR,
            permission_1 INTEGER,
            permission_2 INTEGER,
            permission_3 INTEGER)""")
        con.execute("""
            CREATE TABLE IF NOT EXISTS Сustomers(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            FIO VARCHAR,
            tel VARCHAR,
            date_of_birth VARCHAR)""")
        con.execute("""
            CREATE TABLE IF NOT EXISTS Purchase(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            date INTEGER,
            comment VARCHAR,
            final_price INTEGER,
            is_paid INTEGER,
            FOREIGN KEY (client_id)  REFERENCES Customers (id))
            """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            category VARCHAR,
            price INTEGER,
            is_decaying INTEGER,
            articul INTEGER,
            info_prod VARCHAR GENERATED ALWAYS AS (name || ' ' || category || ' ' || price))""")

        con.execute("""
            CREATE TABLE IF NOT EXISTS Content(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            good_id INTEGER,
            purchase_id INTEGER,
            FOREIGN KEY (purchase_id)  REFERENCES Purchase (id),
            FOREIGN KEY (good_id)  REFERENCES Products (id))
            """)
        con.execute("""
           CREATE TABLE IF NOT EXISTS Warehouses(
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           name VARCHAR,
           location VARCHAR,
           geo_location INTEGER)""")
        con.execute("""
            CREATE TABLE IF NOT EXISTS Delivery(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            good_id INTEGER,
            warehouse_id INTEGER,
            delivery_when INTEGER,
            when_decay INTEGER,
            count INTEGER,
            FOREIGN KEY (warehouse_id)  REFERENCES Warehouses (id),
            FOREIGN KEY (good_id)  REFERENCES Products (id))""")




create_tables("new_bd.db")

