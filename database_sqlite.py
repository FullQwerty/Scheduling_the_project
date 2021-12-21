import sqlite3
import datetime

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    query_tab1 = """ CREATE TABLE IF NOT EXISTS department(id INTEGER, name TEXT) """

    query_tab2 = """ CREATE TABLE IF NOT EXISTS worker(id INTEGER, 
                                                       name TEXT, 
                                                       id_department INTEGER,
                                                       post TEXT,
                                                       id_project INTEGER) """

    query_tab3 = """ CREATE TABLE IF NOT EXISTS project(id INTEGER, name TEXT) """

    query_tab4 = """ CREATE TABLE IF NOT EXISTS deadlines(id INTEGER,
                                                          deadlines_date INTEGER, 
                                                          id_project INTEGER) """

    cursor.execute(query_tab1)
    cursor.execute(query_tab2)
    cursor.execute(query_tab3)
    cursor.execute(query_tab4)

    db.commit()


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

insert_deadlines = [
    (1, get_timestamp(2022, 10, 9), 1),
    (2, get_timestamp(2022, 10, 10), 2)
]

insert_department = [
    (1, 'Front-end'),
    (2, 'Back-end'),
    (3, 'Менеджмент'),
    (4, 'Системный отдел')
]

insert_worker = [
    (1, 'Сидоров Иван Петрович', 1, 'TeamLid', 1),
    (2, 'Иванов Артур Фёдорович', 2, 'TeamLid', 2),
    (3, 'Бабанова Ангелина Григорьевна', 3, 'HR-manager', 3),
    (4, 'Фраус Константин Викторович', 4, 'Системный администратор', 3),
    (5, 'Бабышев Геральт Иосивич', 1, 'Ведущий программист', 1),
    (6, 'Любов Иван Сергеевич', 2, 'Ведущий программист', 2),
    (7, 'Финаников Алексанлдр Максимович', 1, 'Программист junior', 1),
    (8, 'Лобов Максим Анатольевич', 2, 'Программист junior', 2),
    (9, 'Карпов Олег Дмитриевич', 2, 'Программист middle', 1),
    (10, 'Созонов Альберт Викторович', 1, 'Программист middle', 2),
    (11, 'Дружинин Алексанлдр Максимович', 1, 'Программист junior', 1),
    (12, 'Петров Максим Анатольевич', 2, 'Программист junior', 1),
    (13, 'Фиников Олег Дмитриевич', 2, 'Программист middle', 1),
    (14, 'Шастун Альберт Викторович', 1, 'Программист middle', 1)
]

insert_project = [
    (1, 'Разработка сайта для магазина одежды'),
    (2, 'Разработка сайта для магазина автозапчастей'),
    (3, 'Сотрудник не прикреплён не к одному из проектов')
]

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    query_deadlines = """ INSERT INTO deadlines(id, deadlines_date, id_project)
        VALUES(?, ?, ?);"""

    query_department = """ INSERT INTO department(id, name)
        VALUES(?, ?); """

    query_worker = """ INSERT INTO worker(id, name, 
                                          id_department,
                                          post,id_project)
        VALUES(?, ?, ?, ?, ?); """

    query_project = """ INSERT INTO project(id, name)
        VALUES(?, ?); """


    cursor.executemany(query_deadlines, insert_deadlines)
    cursor.executemany(query_department, insert_department)
    cursor.executemany(query_worker, insert_worker)
    cursor.executemany(query_project, insert_project)

    db.commit()







