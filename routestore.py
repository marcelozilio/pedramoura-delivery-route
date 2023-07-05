import sqlite3
import datetime
import uuid

database_path = "pedramoura.db"


def save(route_info):
    # convert flask json type to plain text
    json_text = route_info.get_data(as_text=True)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DeliveryRoute (
            id TEXT PRIMARY KEY,
            route TEXT NOT NULL,
            route_date TEXT NOT NULL
        );
        ''')

    # get current data as route parameter
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    _id = convert_uuid(generate_uuid())

    cursor.execute("INSERT INTO DeliveryRoute (id, route, route_date) VALUES (?, ?, ?)",
                   (_id, json_text, current_date))

    conn.commit()
    cursor.close()
    conn.close()
    return _id


def get_by_id(_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT route FROM DeliveryRoute WHERE id IS '{convert_uuid(_id)}'")
    response = cursor.fetchall()[0][0]

    conn.commit()
    cursor.close()
    conn.close()

    return response


def delete(_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"DELETE from DeliveryRoute WHERE id IS '{convert_uuid(_id)}'")

    conn.commit()
    cursor.close()
    conn.close()

    return {"status": "success"}


def generate_uuid():
    return uuid.uuid4()


def convert_uuid(uuid):
    return str(uuid)
