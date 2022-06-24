import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (name TEXT, place TEXT, date TEXT)")
    connection.commit()


def close():
    connection.close()


def add_entry(entry_name, entry_place, entry_date):
    connection.execute(
        f"INSERT INTO entries(name, place, date) VALUES ('{entry_name}','{entry_place}', '{entry_date}')")
    connection.commit()


def get_entries():
    cursor = connection.cursor()
    return cursor.execute("SELECT * FROM entries")
