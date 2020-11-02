from deprecated import deprecated
import row as row
from flask import jsonify, request, Flask
import sqlite3
from sqlite3 import Error

# app = flask.Flask(__name__)
app = Flask(__name__)
app.config["DEBUG"] = True


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('sqlite.bands')
    except Error as e:
        print("Couldn't connect to database. See error message: " + str(e))

    return conn


@app.route('/', methods=['GET'])
def home():
    return "<h1>List of metal bands</h1><p>This site is a prototype API for the metal bands api</p>"


@app.route('/api/v1/resources/bands', methods=['GET', 'POST'])
def api_bands():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM bands")
        cursor_albums = conn.execute("SELECT "
                                     "l.name, l.record_company "
                                     "FROM albums l "
                                     "INNER JOIN bands b ON "
                                     "b.id=l.band_id")
        albums_db = [
            dict(name=row[0], record_company=row[1])
            for row in cursor_albums.fetchall()
        ]

        bands_db = [
            dict(id=row[0], name=row[1], albums=albums_db, active=row[3])
            for row in cursor.fetchall()
        ]

        if len(bands_db) is not 0:
            return jsonify(bands_db), 200
        else:
            return f"There are no posts in the bands table"

    elif request.method == 'POST':
        new_band = request.json["name"]
        new_active = request.json["active"]

        sql_new_band = """INSERT INTO bands (name, active)
                          VALUES (?, ?)"""
        cursor = cursor.execute(sql_new_band, (new_band, new_active))
        conn.commit()
        return f"Band with id: {cursor.lastrowid} successfully added to the SQLite database", 201


@app.route('/api/v1/resources/band/<int:id_band>', methods=['GET', 'DELETE', 'PUT'])
def api_band(id_band):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM bands where id=?", (id_band,))
        cursor_albums = conn.execute("SELECT "
                                     "l.name, l.record_company "
                                     "FROM albums l "
                                     "INNER JOIN bands b ON "
                                     "b.id=l.band_id "
                                     "WHERE b.id=?", (id_band,))
        albums_db = [
            dict(name=row[0], record_company=row[1])
            for row in cursor_albums.fetchall()
        ]

        band_by_id = [
            dict(id=row[0], name=row[1], albums=albums_db, active=row[3])
            for row in cursor.fetchall()
        ]

        if len(band_by_id) is not 0:
            return jsonify(band_by_id), 200
        else:
            return "Band with id: {} couldn't be found".format(id_band), 404

    if request.method == 'DELETE':
        sql_delete_band = """DELETE FROM bands WHERE id=?"""

        conn.execute(sql_delete_band, (id_band,))
        conn.commit()
        return "Band with id: {} deleted".format(id_band), 200

    if request.method == 'PUT':
        new_id_band = request.json["id"]
        new_name = request.json["name"]
        new_active = request.json["active"]

        sql_put = """UPDATE bands 
                    SET name=?, 
                        active=? 
                    WHERE id=?"""

        conn.execute(sql_put, (new_name, new_active, new_id_band))
        conn.commit()

        updated_band = {
            "id": new_id_band,
            "name": new_name,
            "active": new_active
        }
        return jsonify(updated_band), 200


@app.route('/api/v1/resources/albums', methods=['GET', 'POST'])
def api_albums():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT id, "
                              "name, "
                              "record_company "
                              "FROM albums ")

        albums_db = [
            dict(id=row[0], name=row[1], record_company=row[2])
            for row in cursor.fetchall()
        ]

        if len(albums_db) is not 0:
            return jsonify(albums_db), 200
        else:
            return f"There are no posts in the albums table"

    elif request.method == 'POST':
        new_album_name = request.json["name"]
        new_record_company = request.json["record_company"]
        new_band_id = request.json["band_id"]

        sql_new_album = """INSERT INTO albums (name, record_company, band_id) 
                            VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql_new_album, (new_album_name, new_record_company, new_band_id))
        conn.commit()
        return f"Album with id: {cursor.lastrowid} successfully added to the SQLite database", 201


@app.route('/api/v1/resources/album/<int:id_album>', methods=['GET', 'DELETE', 'PUT'])
def api_album(id_album):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM albums WHERE id=?", (id_album,))
        band_by_id = [
            dict(id=row[0], name=row[1], record_company=row[2])
            for row in cursor.fetchall()
        ]

        if len(band_by_id) is not 0:
            return jsonify(band_by_id), 200
        else:
            return "Band with id: {} couldn't be found".format(id_album), 404

    if request.method == 'DELETE':
        sql_delete_band = """DELETE FROM albums WHERE id=?"""

        conn.execute(sql_delete_band, (id_album,))
        conn.commit()
        return "Album with id: {} deleted".format(id_album), 200

    if request.method == 'PUT':
        new_album_name = request.json["name"]
        new_record_company = request.json["record_company"]

        sql_put = """UPDATE albums 
                    SET name=?, 
                        record_company=? 
                    WHERE id=?"""

        conn.execute(sql_put, (new_album_name, new_record_company, id_album))
        conn.commit()

        updated_album = {
            "id": id_album,
            "name": new_album_name,
            "record_company": new_record_company
        }
        return jsonify(updated_album), 200


app.run(host='0.0.0.0', port=5000)
