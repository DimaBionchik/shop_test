import sqlite3 as sl
import  os
class Data_base_meth:
    DEFAULT_DATABASE_NAME = "new_bd.db"

    def __init__(self, database_name=None):
        self.database_name = database_name or self.DEFAULT_DATABASE_NAME

        self.create_connection()

    def create_connection(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)

        with sl.connect(db_path) as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS Clients(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                telephone VARCHAR,
                date_of_birth DATE)
            """)
    def create_connectionn(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)

        with sl.connect(db_path) as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS Операции(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name_operation VARCHAR,
                who_fio VARCHAR,
                date_of_birth DATE)
            """)

    def get_comu_name(self):
        conne = sl.connect("new_bd.db")
        cur = conne.cursor()
        table_name = "Продукты"
        sqlc = f"PRAGMA table_info({table_name})"
        field_info = list(cur.execute(sqlc))
        field_names = [info[1] for info in field_info]
        conne.close()
        return field_names



    def search_in_db(self, keyword):
        comm  = self.get_comu_name()

        query = f"SELECT * FROM Продукты WHERE {' OR '.join([f'{field} LIKE ?' for field in comm])}"
        print("Query:", query)

        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cur = con.cursor()
            try:
                cur.execute(query, tuple([f'%{keyword}%' for _ in range(len(comm))]))
            except sl.Error as e:
                print("SQLite error:", e)
            result = cur.fetchall()

        return result

    def show_all_from_table(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute(""" SELECT * FROM Продукты""")

    def insert_user_data(self, name, category, price,is_dec,art):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute("""
                INSERT INTO Продукты (name, category, price,when_decay,articul) 
                VALUES (?, ?, ?,?,?);
            """, (str(name), category, price,is_dec,art))

    def insert_sklad_data(self, name, location, geo):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute("""
                   INSERT INTO Склады (name, location, geo_location) 
                   VALUES (?, ?, ?);
               """, (str(name), location, geo))

    def select_all_from_db(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM Продукты""")
            result = cursor.fetchall()
        return result
    def select_all_from_sclad(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM Склады""")
            result = cursor.fetchall()
        return result


    def select_sclad(self,name):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute(f""" SELECT id FROM Склады where name ='{name}'""")
            result = cursor.fetchall()
            value = result[0][0]
        return value

    def select_client_id(self,name):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute(f""" SELECT id FROM Клиенты where FIO ='{name}'""")
            result = cursor.fetchall()
            print(result)
            value = result[0][0]
            print(value)
        return value
    def inser_into_deliver(self,sclad,date,basket):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute("""
                           INSERT INTO Поставка (warehouse_id, delivery_when, busket) 
                           VALUES (?, ?, ?);
                       """, (sclad, date, basket))

    def inser_into_sell_operation(self,client,date,price,is_pa,basket):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute("""
                           INSERT INTO Покупка (client_id, date, final_price,is_paid,busket) 
                           VALUES (?, ?, ?,?,?);
                       """, (client, date, price,is_pa,basket))


    def select_price(self,name):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute(f""" SELECT price FROM Продукты WHERE name = '{name}'""")
            result = cursor.fetchall()
            value = result[0][0]
        return value

    def select_all_from_client(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM Клиенты""")
            result = cursor.fetchall()
        return result

    def inser_into_deliverr(self):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute("""
                           INSERT INTO Клиенты (FIO, tel, date_of_birth) 
            VALUES ('Сидоров Сидор', '987654321', '1980-05-15'),
                   ('Алексеев Алексей', '555-123-456', '1995-10-20')""")

    def inser_into_clietn(self,fio,tel,data):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            con.execute("""
                           INSERT INTO Клиенты (FIO, tel, date_of_birth) 
                           VALUES (?, ?, ?);
                       """, (fio, tel, data))

    def inser_into_operation(self,name,who,when):
            db_path = os.path.join(os.path.dirname(__file__), self.database_name)
            with sl.connect(db_path) as con:
                con.execute("""
                               INSERT INTO Операции (name_operation,who_fio,date_of_delivery) 
                               VALUES (?, ?, ?);
                           """, (name, who, when))



    def update_basket(self,busket,sclad):
        db_path = os.path.join(os.path.dirname(__file__), self.database_name)
        with sl.connect(db_path) as con:
            cursor = con.cursor()
            cursor.execute("UPDATE Склады SET busket = ? WHERE id = ?", (busket, sclad))

# data = Data_base_meth(database_name="new_bd.db")
# data.create_connectionn()
