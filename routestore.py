import sqlite3
import datetime

database_path = "pedramoura.db"

def save(route_info):
    # convert flask json type to plain text
    json_text = route_info.get_data(as_text=True) 

    # connect to db (local file)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DeliveryRoute (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            route TEXT NOT NULL,
            route_date TEXT NOT NULL
        );
        ''')

    # get current data as route parameter
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    # insert json text into table
    cursor.execute("INSERT INTO DeliveryRoute (route, route_date) VALUES (?, ?)", (json_text, current_date))

    # commit to db
    conn.commit()


    # debug only, query data from RotaEntrega
    # cursor.execute("SELECT id, route_date FROM DeliveryRoute")
    # for route in cursor.fetchall():
    #     print(route)

    # close database
    cursor.close()
    conn.close()


def load(id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT route FROM DeliveryRoute WHERE id IS {id}")
    return cursor.fetchall()[0][0]
