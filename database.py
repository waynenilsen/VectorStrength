import sqlite3


def connect():
    return sqlite3.connect('static/database.db')


def add_record(data):
    with connect() as conn:
        res = conn.execute('''
        INSERT INTO data (x, y, z, alpha, beta, gamma, utc_set_start_time, utc_measure_time, fk_activity)
        VALUES (:x,
                :y,
                :z,
                :alpha,
                :beta,
                :gamma,
                :utc_set_start_time,
                :utc_measure_time,
                :fk_activity);
        ''', data)



