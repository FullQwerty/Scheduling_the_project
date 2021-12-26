import sqlite3
import datetime


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

def get_string_timestamp(s):
    t = s.split('-')
    return get_timestamp(int(t[0]), int(t[1]), int(t[2]))


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
        query = """ SELECT worker.worker_id, 
                worker.name_worker, 
                worker.post, 
                project.name_project, 
                department.name_department 
                FROM worker JOIN project, department
                WHERE project.project_id = worker.project_id 
                AND department.department_id = worker.department_id"""
        cursor.execute(query)
        records = cursor.fetchall()

        for row in records:
            data_staff.append(row)
        return data_staff
        cursor.close()

def get_combobox(table):
    ls = []
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query_project_table = """ SELECT name_project FROM project """
        query_worker_table = """ SELECT name_worker FROM worker """
        if table == 'project':
            cursor.execute(query_project_table)
        elif table == 'worker':
            cursor.execute(query_worker_table)
        else:
            return print('Ошибка ! Такой таблицы в базе данных не существует')

        ls=list(cursor)
        return ls
        cursor.close()

#get_combobox('project')

