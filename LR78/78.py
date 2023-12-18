import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import psycopg2


class InputMask:
    def __init__(self, mask, entry):
        self.mask = mask
        self.entry = entry
        self.placeholder = '#'
        self.bindings = entry.bindtags()
        self.old_validate = entry['validate']
        entry.bind('<KeyPress>', self.on_keypress)
        entry.bind('<KeyRelease>', self.on_keyrelease)
        entry.bind('<FocusIn>', self.on_focusin)
        entry.bind('<FocusOut>', self.on_focusout)
        entry['validatecommand'] = (entry.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        entry.set(mask)

    def validate(self, action, index, char, P, V, W):
        if action == '1':
            return all(c == self.placeholder or c.isdigit() for c in P)
        return True

    def on_keypress(self, event):
        if event.char.isprintable():
            current_text = self.entry.get()
            index = self.entry.index(tk.INSERT)
            next_char = self.mask[index]
            if next_char == self.placeholder or next_char.isdigit():
                current_text = current_text[:index] + event.char + current_text[index + 1:]
                if not self.validate('1', index, event.char, current_text, current_text, None):
                    return 'break'

    def on_keyrelease(self, event):
        current_text = self.entry.get()
        for c in current_text:
            if c.isdigit() or c == self.placeholder:
                continue
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.mask)
            break

    def on_focusin(self, event):
        self.entry.bindtags(self.bindings + ('focusin',))
        self.entry['validate'] = 'key'
        self.entry.set(self.entry.get())

    def on_focusout(self, event):
        self.entry.bindtags(self.bindings)
        self.entry['validate'] = self.old_validate
        self.entry.set(self.entry.get())

class DatabaseInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Интерфейс базы данных")

        try:
            # Подключение к базе данных
            self.conn = psycopg2.connect(
                dbname='LR5',
                user='postgres',
                password='gcc2020',
                host='localhost',
                port='5432'
            )
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться к базе данных: {e}")
            self.master.destroy()
            return

        self.tables = {
            "applicant": {"columns": ["id_applicant", "surname", "name", "patronymic", "date_of_birth", "city_residence", "email", "phone_number"]},
            "contract": {"columns": ["contract_number", "term_of_the_agreement", "id_applicant", "id_employer", "date_of_conclusion_contract", "cost_of_providing_services", "contract_with_the_employer"]},
            "employer": {"columns": ["id_employer", "company_name", "email", "ur_adres", "inn", "ogrn", "kpp"]},
            "job_openings": {"columns": ["id_job_opening", "id_employer", "required_education", "required_work_experience", "salary", "specialty"]},
            "resume": {"columns": ["id_resume", "education", "id_applicant", "work_experience", "specialty", "desired_city_of_work"]}
        }

        self.tabs = ["applicant", "contract", "employer", "job_openings", "resume"]

        self.russian_table_names = {
            "applicant": "Заявители",
            "contract": "Договоры",
            "employer": "Работодатели",
            "job_openings": "Вакансии",
            "resume": "Резюме"
        }

        self.russian_column_names = {
            "id_applicant": "ID заявителя",
            "surname": "Фамилия",
            "name": "Имя",
            "patronymic": "Отчество",
            "date_of_birth": "Дата рождения",
            "city_residence": "Город проживания",
            "email": "Email",
            "phone_number": "Номер телефона",
            "contract_number": "Номер договора",
            "term_of_the_agreement": "Срок договора",
            "id_employer": "ID работодателя",
            "date_of_conclusion_contract": "Дата заключения договора",
            "cost_of_providing_services": "Стоимость предоставления услуг",
            "contract_with_the_employer": "Договор с работодателем",
            "company_name": "Название компании",
            "ur_adres": "Юридический адрес",
            "inn": "ИНН",
            "ogrn": "ОГРН",
            "kpp": "КПП",
            "id_job_opening": "ID вакансии",
            "required_education": "Требуемое образование",
            "required_work_experience": "Требуемый опыт работы",
            "salary": "Заработная плата",
            "specialty": "Специальность",
            "id_resume": "ID резюме",
            "education": "Образование",
            "work_experience": "Опыт работы",
            "desired_city_of_work": "Желаемый город работы"
        }

        self.create_widgets()

    def create_masked_entry(self, master, mask):
        entry_var = tk.StringVar()
        entry = ttk.Entry(master, textvariable=entry_var, font='TkDefaultFont')

        masker = InputMask(mask, entry_var)
        masker.bind_to(entry)

        return entry

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self.master)
        self.treeviews = {}

        for table_name in self.tabs:
            frame = ttk.Frame(self.tab_control)
            self.tab_control.add(frame, text=self.russian_table_names.get(table_name, table_name.capitalize()))

            columns = self.tables[table_name]["columns"][1:]  # Исключаем первый столбец, так как это id
            self.treeviews[table_name] = ttk.Treeview(frame, columns=columns, show="headings")

            for col in columns:
                # Замените английские названия столбцов на русские
                russian_col_name = self.russian_column_names.get(col, col)
                self.treeviews[table_name].heading(col, text=russian_col_name)
                self.treeviews[table_name].column(col, anchor=tk.CENTER)

            ysb = ttk.Scrollbar(frame, orient="vertical", command=self.treeviews[table_name].yview)
            xsb = ttk.Scrollbar(frame, orient="horizontal", command=self.treeviews[table_name].xview)
            self.treeviews[table_name].configure(yscroll=ysb.set, xscroll=xsb.set)

            ysb.pack(side="right", fill="y")
            xsb.pack(side="bottom", fill="x")
            self.treeviews[table_name].pack(expand=1, fill="both")

            button_add = ttk.Button(frame, text=f"Добавить {self.russian_table_names.get(table_name, table_name.capitalize())}", command=lambda tn=table_name: self.add_record_dialog(tn))
            button_add.pack(side="bottom")

            button_edit = ttk.Button(frame, text=f"Редактировать {self.russian_table_names.get(table_name, table_name.capitalize())}", command=lambda tn=table_name: self.edit_record_dialog(tn))
            button_edit.pack(side="bottom")

            button_delete = ttk.Button(frame, text=f"Удалить {self.russian_table_names.get(table_name, table_name.capitalize())}", command=lambda tn=table_name: self.delete_record(tn))
            button_delete.pack(side="bottom")

        self.tab_control.pack(expand=1, fill="both")

        self.refresh_lists()

    def create_dropdown(self, master, query, values_column):
        self.cursor.execute(query)
        items = self.cursor.fetchall()

        var = tk.StringVar(master)
        dropdown = ttk.Combobox(master, textvariable=var, state="readonly")

        # Используем list comprehension для получения списка значений из кортежей
        values = [item[values_column] for item in items]
        dropdown["values"] = values

        dropdown.pack()
        return dropdown

    def create_applicant_dropdown(self, master):
        query = "SELECT id_applicant, surname, name, patronymic FROM applicant;"
        return self.create_dropdown(master, query, values_column=1)

    def create_employer_dropdown(self, master):
        query = "SELECT id_employer, company_name FROM employer;"
        return self.create_dropdown(master, query, values_column=1)  # Используем values_column=1

  


    def add_record_dialog(self, table_name):
        dialog = tk.Toplevel(self.master)
        dialog.title(f"Добавить запись в {self.russian_table_names.get(table_name, table_name.capitalize())}")

        labels = self.tables[table_name]["columns"][1:]  # Исключаем первый столбец, так как это id
        entries = []

        for label in labels:
            tk.Label(dialog, text=self.russian_column_names.get(label, label)).pack()

            # Добавляем выбор даты календарем
            if label in ["date_of_birth", "date_of_conclusion_contract"]:
                entry = DateEntry(dialog, width=12, background='darkblue', foreground='white', borderwidth=2)
            elif label == "phone_number":
                entry = tk.Entry(dialog)
            elif label == "id_applicant":
                entry = self.create_applicant_dropdown(dialog)
            elif label == "id_employer":
                entry = self.create_employer_dropdown(dialog)  # Используем create_employer_dropdown
                entry.pack_forget()  # Скрываем поле ID работодателя
            elif label == "id_job_opening":
                entry = self.create_job_opening_dropdown(dialog)  # Добавим функцию создания выпадающего списка для вакансий
            else:
                entry = tk.Entry(dialog)

            entry.pack()
            entries.append(entry)

        tk.Button(dialog, text="Добавить", command=lambda: self.add_record_to_db(dialog, table_name, entries)).pack()


        

    def edit_record_dialog(self, table_name):
        selected_item = self.treeviews[table_name].selection()

        if not selected_item:
            messagebox.showinfo("Предупреждение", "Выберите запись для редактирования.")
            return

        item_values = self.treeviews[table_name].item(selected_item, 'values')
        record_id = item_values[0]

        try:
            record_id = int(record_id)  # Преобразование к целому числу
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ID записи")
            return

        if record_id <= 0:
            messagebox.showerror("Ошибка", "Неверный ID записи")
            return

        dialog = tk.Toplevel(self.master)
        dialog.title(f"Редактировать запись в {self.russian_table_names.get(table_name, table_name.capitalize())}")

        labels = self.tables[table_name]["columns"][1:]  # Исключаем первый столбец, так как это id
        entries = []

        for i, label in enumerate(labels):
            tk.Label(dialog, text=self.russian_column_names.get(label, label)).pack()

            if label in ["date_of_birth", "date_of_conclusion_contract"]:
                entry = DateEntry(dialog, width=12, background='darkblue', foreground='white', borderwidth=2)
                entry.set(self.convert_to_date(item_values[i]))
            elif label == "phone_number":
                entry = tk.Entry(dialog)
                entry.insert(0, item_values[i])
            elif label == "id_applicant":
                entry = self.create_applicant_dropdown(dialog)
            elif label == "id_employer":
                entry = self.create_employer_dropdown(dialog)  # Используем create_employer_dropdown
                entry.pack_forget()  # Скрываем поле ID работодателя
            else:
                entry = tk.Entry(dialog)
                entry.insert(0, item_values[i])

            entry.pack()
            entries.append(entry)

        tk.Button(dialog, text="Сохранить", command=lambda: self.edit_record_in_db(dialog, table_name, selected_item, record_id, entries)).pack()

    def add_record_to_db(self, dialog, table_name, entries):
        values = [entry.get() for entry in entries]
        dialog.destroy()

        if not all(values):
            return

        # Обработка дат перед сохранением в базу данных
        for i, label in enumerate(self.tables[table_name]["columns"][1:]):
            if label in ["date_of_birth", "date_of_conclusion_contract"]:
                date_value = self.convert_to_date(values[i])
                if date_value is not None:
                    values[i] = date_value
                else:
                    values[i] = None

        columns = ", ".join(self.tables[table_name]["columns"][1:])  # Исключаем первый столбец, так как это id
        placeholders = ", ".join(["%s" if value is not None else "NULL" for value in values])

        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

        try:
            self.cursor.execute(insert_query, values)
            self.conn.commit()
            self.refresh_lists()
            messagebox.showinfo("Успех", "Запись успешно добавлена.")
        except psycopg2.Error as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить запись: {e}")

    def edit_record_in_db(self, dialog, table_name, selected_item, record_id, entries):
        values = [entry.get() for entry in entries]
        dialog.destroy()

        if not all(values):
            return

        # Обработка дат перед сохранением в базу данных
        for i, label in enumerate(self.tables[table_name]["columns"][1:]):
            if label in ["date_of_birth", "date_of_conclusion_contract"]:
                date_value = self.convert_to_date(values[i])
                if date_value is not None:
                    values[i] = date_value
                else:
                    values[i] = None

        set_clause = ", ".join([f"{col} = %s" if val is not None else f"{col} = NULL" for col, val in zip(self.tables[table_name]["columns"][1:], values)])

        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {self.tables[table_name]['columns'][0]} = %s;"

        try:
            self.cursor.execute(update_query, values + [record_id])
            self.conn.commit()
            self.refresh_lists()
            messagebox.showinfo("Успех", f"Запись успешно отредактирована.")
        except psycopg2.Error as e:
            messagebox.showerror("Ошибка", f"Не удалось отредактировать запись: {e}")

    def delete_record(self, table_name):
            selected_item = self.treeviews[table_name].selection()

            if not selected_item:
                messagebox.showinfo("Предупреждение", "Выберите запись для удаления.")
                return

            confirmation = messagebox.askokcancel("Подтверждение", "Вы уверены, что хотите удалить выбранную запись?")
            if not confirmation:
                return

            item_values = self.treeviews[table_name].item(selected_item, 'values')
            record_id = item_values[0]

            try:
                record_id = int(record_id)  # Преобразование к целому числу
            except ValueError:
                messagebox.showerror("Ошибка", "Неверный ID записи")
                return

            if record_id <= 0:
                messagebox.showerror("Ошибка", "Неверный ID записи")
                return

            delete_query = f"DELETE FROM {table_name} WHERE {self.tables[table_name]['columns'][0]} = %s;"

            try:
                self.cursor.execute(delete_query, [record_id])
                self.conn.commit()
                self.refresh_lists()
                messagebox.showinfo("Успех", "Запись успешно удалена.")
            except psycopg2.Error as e:
                messagebox.showerror("Ошибка", f"Не удалось удалить запись: {e}")

    def refresh_lists(self):
            for table_name in self.tabs:
                self.treeviews[table_name].delete(*self.treeviews[table_name].get_children())
                self.cursor.execute(f"SELECT * FROM {table_name};")
                rows = self.cursor.fetchall()

                for row in rows:
                    self.treeviews[table_name].insert("", "end", values=row)

    def convert_to_date(self, date_str):
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                return date_obj
            except ValueError:
                return None

    def create_job_opening_dropdown(self, master):
            query = "SELECT id_job_opening, specialty FROM job_openings;"
            return self.create_dropdown(master, query, values_column=1)

if __name__ == "__main__":
        root = tk.Tk()
        app = DatabaseInterface(root)
        root.mainloop()
    