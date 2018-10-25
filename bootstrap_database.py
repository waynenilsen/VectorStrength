import database


def bootstrap():
    with database.connect() as conn:
        conn.execute('''
        create table data (
            x real,
            y real,
            z real,
            alpha real,
            beta real,
            gamma real,
            utc_set_start_time int,
            utc_measure_time int,
            fk_activity int 
        )
        ''')

if __name__ == '__main__':
    bootstrap()