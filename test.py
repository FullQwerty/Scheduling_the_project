import sqlite3
import datetime

def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

def get_staff_inf():
    worker=[]
    with sqlite3.connect('database.db') as db:
        cursor_for_worker = db.cursor()
        cursor_for_deadlines = db.cursor()

        query_worker = """ SELECT * FROM worker"""
        query_deadlines = """ SELECT * FROM deadlines"""

        cursor_for_worker.execute(query_worker)
        cursor_for_deadlines.execute(query_deadlines)

        records_worker = cursor_for_worker.fetchall()
        records_deadlines = cursor_for_deadlines.fetchall()

        for row in records_worker:
            worker.append(row[4])
        print(worker)

        for row in records_deadlines:


        cursor_for_worker.close()
        cursor_for_deadlines.close()

get_staff_inf()