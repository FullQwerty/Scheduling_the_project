import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
import project_helper as ph


window = tk.Tk()
window.title('Расписание выполнения проектов')

frame_add_form = tk.Frame(window, bg='green')
frame_statistic = tk.Frame(window, bg='yellow')
frame_list = tk.Frame(window, bg='blue')

frame_add_form.grid(column=0, row=0, sticky="ns")
frame_statistic.grid(column=1, row=0)
frame_list.grid(column=0, row=1, columnspan=2, sticky="we")

#items = [0, 1, 2, 3, 4]

def form_submit():
    project=f_project.get()
    dl=ph.get_string_timestamp(f_deadline.get())
    stff=f_staff.get()
    insert_ = (project, dl, stff)
    print(insert_)
    print(ph.get_date(dl))
    print(type(project), type(dl), type(stff))

    #with sqlite3.connect('database.db') as db:
        #cursor = db.cursor()
        #query_worker = """ INSERT INTO """

l_project = ttk.Label(frame_add_form, text="Выбор проекта")
f_project = ttk.Combobox(frame_add_form, values=ph.get_combobox('project'))
l_deadline = ttk.Label(frame_add_form, text="Deadline")
f_deadline = DateEntry(frame_add_form, foreground='black', normalforeground='black',
                                        selectforeground='red', background='white',
                                        date_pattern='YYYY-mm-dd')
l_staff = ttk.Label(frame_add_form, text="Назначить сотрудника ")
f_staff = ttk.Combobox(frame_add_form, values=ph.get_combobox('worker'))
btn_submit = ttk.Button(frame_add_form, text="Добавить", command=form_submit)

l_project.grid(row=0, column=0, sticky='w', padx=10, pady=10)
f_project.grid(row=0, column=1, sticky='e', padx=10, pady=10)
l_deadline.grid(row=1, column=0, sticky='w', padx=10, pady=10)
f_deadline.grid(row=1, column=1, sticky='e', padx=10, pady=10)
l_staff.grid(row=2, column=0, sticky='w', padx=10, pady=10)
f_staff.grid(row=2, column=1, sticky='e', padx=10, pady=10)
btn_submit.grid(row=3, column=0, columnspan=2, sticky='n', padx=10, pady=10)

l_completeness_text = tk.Label(frame_statistic, text='Текущее состояние', font="Helvetica 14")
l_nearest_dl_text = tk.Label(frame_statistic, text='Ближайший дедлайн:', font="Helvetica 14")
l_nearest_dl_value = tk.Label(frame_statistic, text=ph.get_date(ph.get_deadline()), font="Helvetica 14 bold")
l_number_staff_text = tk.Label(frame_statistic, text='Число сотрудников на проекте:', font="Helvetica 14")
l_number_staff_value = tk.Label(frame_statistic, text=ph.get_staff_inf(), font="Helvetica 14 bold")

l_completeness_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
l_nearest_dl_text.grid(row=1, column=0, sticky="w", padx=10, pady=10)
l_nearest_dl_value.grid(row=1, column=1, sticky="e", padx=10, pady=10)
l_number_staff_text.grid(row=2, column=0, sticky="w", padx=10, pady=10)
l_number_staff_value.grid(row=2, column=1, sticky="e", padx=10, pady=10)

#l_temp_frame_add_form = tk.Label(frame_add_form, text="календарь", font="Helvetica 14")
#l_temp_frame_add_form.pack(expand=True, padx=20, pady=20)

heads = ['id-сотрудника', 'ФИО', 'id-отдела', 'Должность', 'id-проекта']
table = ttk.Treeview(frame_list, show='headings')
table['columns'] = heads

for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

for row in ph.get_table_data():
    table.insert('', tk.END, values=row)

scroll_pane = ttk.Scrollbar(frame_list, command=table.yview())
table.configure(yscrollcommand=scroll_pane.set)
scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)


table.pack(expand=tk.YES, fill=tk.BOTH)

window.mainloop()
