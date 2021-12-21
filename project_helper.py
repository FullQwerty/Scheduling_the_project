import sqlite3
import datetime


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


def get_staff_inf():
    worker = []
    count = 0
    id_proj_worker = 0
    dl_staff = get_deadline()


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

        for row in records_deadlines:
            if row[1] == dl_staff:
                id_proj_worker = row[2]
            else:
                pass

        for item in worker:
            if item == id_proj_worker:
                count+=1
            else:
                pass
        return count

        cursor_for_worker.close()
        cursor_for_deadlines.close()

def get_deadline():
    dl = []
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM deadlines"""
        cursor.execute(query)
        records = cursor.fetchall()

        for row in records:
            dl.append(row[1])
        return min(dl)
        cursor.close()

def get_table_data():
    data_staff=[]
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM worker"""
        cursor.execute(query)
        records = cursor.fetchall()

        for row in records:
            data_staff.append(row)
        return data_staff
        cursor.close()


