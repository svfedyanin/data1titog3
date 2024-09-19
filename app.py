from faker import Faker
import psycopg2

def workWithDb(user, password, host, port, database):

    try:
        conn = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
        queryCreateDb = """CREATE TABLE test_table (
                                        id SERIAL PRIMARY KEY,
                                        name VARCHAR(30),
                                        age INTEGER,
                                        Department VARCHAR(140)
                        );"""

        with conn.cursor() as curs:
            curs.execute(queryCreateDb)
            fake = Faker()
            for i in range(10):
                name = fake.first_name()
                age = fake.random_int(min=18, max=60)
                department = fake.job()
                querySqlInsert = f"INSERT INTO test_table(name, age, department) VALUES ('{name}', {age}, '{department}')"
                curs.execute(querySqlInsert)

            querySqlSelect = f"SELECT * FROM test_table"
            curs.execute(querySqlSelect)
            for row in curs.fetchall():
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


if __name__ == "__main__":
    db_user = 'postgres'
    db_password = 'password'
    db_host = 'db'
    db_port = '5432'
    db_name = 'fedyanin'
    workWithDb(db_user, db_password, db_host, db_port, db_name)