import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
import project_helper as ph

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Составления расписания выполнения проекта')
        self['background'] = '#EBEBEB'
        self.conf = {'padx':(10, 30), 'pady':10}
        self.bold_font = 'Helvetica 13 bold'
        self.put_frames()

    def put_frames(self):
        self.add_form_frame = AddForm(self).grid(row=0, column=0, sticky='nswe')
        self.stat_frame = StatFrame(self).grid(row=0, column=1, sticky='nswe')
        self.table_frame = TableFrame(self).grid(row=1, column=0, columnspan=2,
                                                                    sticky='nswe')

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()

class AddForm(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.l_project = ttk.Label(self, text="Выбор проекта")
        self.f_project = ttk.Combobox(self, values=ph.get_combobox('project'))
        self.l_deadline = ttk.Label(self, text="Deadline")
        self.f_deadline = DateEntry(self, foreground='black', normalforeground='black',
                               selectforeground='red', background='white',
                               date_pattern='YYYY-mm-dd')
        self.l_staff = ttk.Label(self, text="Назначить сотрудника ")
        self.f_staff = ttk.Combobox(self, values=ph.get_combobox('worker'))
        self.btn_submit = ttk.Button(self, text="Добавить", command=self.form_submit)

        self.l_project.grid(row=0, column=0, sticky='w', cnf=self.master.conf)
        self.f_project.grid(row=0, column=1, sticky='e', cnf=self.master.conf)
        self.l_deadline.grid(row=1, column=0, sticky='w', cnf=self.master.conf)
        self.f_deadline.grid(row=1, column=1, sticky='e', cnf=self.master.conf)
        self.l_staff.grid(row=2, column=0, sticky='w', cnf=self.master.conf)
        self.f_staff.grid(row=2, column=1, sticky='e', cnf=self.master.conf)
        self.btn_submit.grid(row=3, column=0, columnspan=2, sticky='n', cnf=self.master.conf)

    def form_submit(self):
        project = self.f_project.get()
        dl = int(ph.get_string_timestamp(self.f_deadline.get()))
        stff = self.f_staff.get()
        insert_ = (project, dl, stff)
        count=1
        if count==1:
            mb.askyesno(
                title='Информация о БД',
                message='Получены ноыые данные о проектах, внести их?'
            )
            print('В базу данных внесены поправки: ', insert_, '\n',
                                                    ph.get_date(dl), '\n', type(project), type(dl), type(stff))
            self.master.refresh()

class StatFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        l_completeness_text = tk.Label(self, text='Текущее состояние')
        l_nearest_dl_text = tk.Label(self, text='Ближайший дедлайн:')
        l_nearest_dl_value = tk.Label(self, text=ph.get_date(ph.get_deadline()),
                                                                    font=self.master.bold_font)
        l_number_staff_text = tk.Label(self, text='Число сотрудников на проекте:')
        l_number_staff_value = tk.Label(self, text=ph.get_staff_inf(), font=self.master.bold_font)

        l_completeness_text.grid(row=0, column=0, columnspan=2, cnf=self.master.conf)
        l_nearest_dl_text.grid(row=1, column=0, sticky="w", cnf=self.master.conf)
        l_nearest_dl_value.grid(row=1, column=1, sticky="e", cnf=self.master.conf)
        l_number_staff_text.grid(row=2, column=0, sticky="w", cnf=self.master.conf)
        l_number_staff_value.grid(row=2, column=1, sticky="e", cnf=self.master.conf)


class TableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        heads = ['id-сотрудника', 'ФИО', 'id-отдела', 'Должность', 'id-проекта']
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in ph.get_table_data():
            table.insert('', tk.END, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview())
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)

        table.pack(expand=tk.YES, fill=tk.BOTH)



app = App()
app.mainloop()