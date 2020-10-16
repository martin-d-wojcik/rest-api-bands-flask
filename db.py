import sqlite3

conn = sqlite3.connect('sqlite.bands')

cursor = conn.cursor()
sql_create_bands_table = """ CREATE TABLE IF NOT EXISTS bands (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        albums text,
                                        active boolean
                                    ); """
sql_create_albums_table = """CREATE TABLE IF NOT EXISTS albums (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,    
                                    record_company text,
                                    band_id integer,
                                    FOREIGN KEY (band_id) REFERENCES bands (id)
                                );"""
cursor.execute(sql_create_bands_table)
cursor.execute(sql_create_albums_table)