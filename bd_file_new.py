import sqlite3 as sl

def create_tables(name_of_bd:str):
    connect = sl.connect(name_of_bd)
    with connect as con :
        con.execute("""
            CREATE TABLE IF NOT EXISTS Сотрудники(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            login VARCHAR,
            password VARCHAR,
            permission_1 INTEGER,
            permission_2 INTEGER,
            permission_3 INTEGER)""")

        con.execute("""
            CREATE TABLE IF NOT EXISTS Клиенты(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            FIO VARCHAR,
            tel VARCHAR,
            date_of_birth VARCHAR)""")

        con.execute("""
            CREATE TABLE IF NOT EXISTS Покупка(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            date INTEGER,
            final_price INTEGER,
            is_paid INTEGER,
            busket VARCHAR,
            FOREIGN KEY (client_id) REFERENCES Клиенты(id))""")

        con.execute("""
            CREATE TABLE IF NOT EXISTS Продукты(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            category VARCHAR,
            price INTEGER,
            when_decay INTEGER,
            articul INTEGER)""")

        con.execute("""
           CREATE TABLE IF NOT EXISTS Склады(
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           name VARCHAR,
           location VARCHAR,
           geo_location INTEGER)""")

        con.execute("""
            CREATE TABLE IF NOT EXISTS Поставка(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER,
            delivery_when INTEGER,
            busket VARCHAR,
            FOREIGN KEY (warehouse_id) REFERENCES Склады(id))""")



create_tables("new_bd.db")

