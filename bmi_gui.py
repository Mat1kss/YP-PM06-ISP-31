import tkinter as tk
from tkinter import messagebox
import bmi_func as core

class BmiApplication(tk.Frame):
    def __init__(self, master=None):
        # Инициализируем базовый контейнер Frame
        super().__init__(master)
        
        self.master = master
        self.master.title("Расчет ИМТ")
        
        # ИСПРАВЛЕНИЕ: Ширина окна увеличена до 640 пикселей, чтобы длинный текст не обрезался
        self.master.geometry("640x480+250+150")
        self.master.configure(bg="#d4d0c8")  # Классический серый цвет Windows Classic
        self.master.overrideredirect(True)
        
        # Переменные для перетаскивания окна мышкои
        self._offsetx = 0
        self._offsety = 0
        
        # Привязка системного события для восстановления ретро-рамок при разворачивании окна
        self.master.bind("<Map>", self.restore_window)
        
        # Сборка интерфейса
        self.build_custom_title_bar()
        self.build_interface_components()
        self.refresh_history_view()

    def build_custom_title_bar(self):
        """Создание ретро темно-синей панели заголовка."""
        title_bar = tk.Frame(self.master, bg="#004e98", height=26, relief="raised", bd=1)
        title_bar.pack(fill="x", side="top")
        title_bar.pack_propagate(False)
        
        title_bar.bind("<Button-1>", self.click_title_bar)
        title_bar.bind("<B1-Motion>", self.drag_title_bar)
        
        title_label = tk.Label(title_bar, text="Расчёт индекса массы тела (ИМТ)", 
                               fg="white", bg="#004e98", font=("Arial", 10, "bold"))
        title_label.pack(side="left", padx=5)
        title_label.bind("<Button-1>", self.click_title_bar)
        title_label.bind("<B1-Motion>", self.drag_title_bar)
        
        close_btn = tk.Button(title_bar, text=" ✕ ", bg="#d4d0c8", fg="black", bd=1,
                              font=("Arial", 8, "bold"), relief="raised", command=self.master.destroy)
        close_btn.pack(side="right", padx=2, pady=2)
        
        minimize_btn = tk.Button(title_bar, text=" — ", bg="#d4d0c8", fg="black", bd=1,
                                 font=("Arial", 8, "bold"), relief="raised", command=self.minimize_window)
        minimize_btn.pack(side="right", pady=2)

    def click_title_bar(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def drag_title_bar(self, event):
        x = self.master.winfo_x() + event.x - self._offsetx
        y = self.master.winfo_y() + event.y - self._offsety
        self.master.geometry(f'+{x}+{y}')

    def minimize_window(self):
        """Безопасное сворачивание программы на панель задач Windows."""
        self.master.overrideredirect(False)
        self.master.iconify()

    def restore_window(self, event=None):
        """Автоматическое скрытие рамок ОС при разворачивании окна из панели."""
        if self.master.wm_state() == "normal":
            self.master.overrideredirect(True)

    def build_interface_components(self):
        """Построение элементов графического интерфейса по референсу Windows Classic."""
        main_container = tk.Frame(self.master, bg="#d4d0c8", bd=2, relief="flat")
        main_container.pack(fill="both", expand=True, padx=8, pady=8)
        
        top_row = tk.Frame(main_container, bg="#d4d0c8")
        top_row.pack(fill="x", side="top", pady=2)
        
        # Блок 1: Исходные данные
        frame_inputs = tk.LabelFrame(top_row, text="Исходные данные", bg="#d4d0c8", 
                                     font=("Arial", 9, "bold"), bd=2, relief="groove")
        frame_inputs.pack(side="left", fill="both", expand=True, padx=2, pady=2)
        
        tk.Label(frame_inputs, text="Вес, кг:", bg="#d4d0c8", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=6, sticky="w")
        self.entry_weight = tk.Entry(frame_inputs, bd=2, relief="sunken", width=14, bg="white")
        self.entry_weight.grid(row=0, column=1, padx=5, pady=6)
        
        btn_calc = tk.Button(frame_inputs, text="Рассчитать", width=12, bd=2, relief="raised", activebackground="#d4d0c8", command=self.execute_calculation)
        btn_calc.grid(row=0, column=2, padx=10, pady=6)
        
        tk.Label(frame_inputs, text="Рост, см:", bg="#d4d0c8", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=6, sticky="w")
        self.entry_height = tk.Entry(frame_inputs, bd=2, relief="sunken", width=14, bg="white")
        self.entry_height.grid(row=1, column=1, padx=5, pady=6)
        
        btn_clear = tk.Button(frame_inputs, text="Очистить", width=12, bd=2, relief="raised", activebackground="#d4d0c8", command=self.execute_clear)
        btn_clear.grid(row=1, column=2, padx=10, pady=6)
        
        # Блок 2: Результат
        frame_result = tk.LabelFrame(top_row, text="Результат", bg="#d4d0c8", 
                                      font=("Arial", 9, "bold"), bd=2, relief="groove")
        frame_result.pack(side="right", fill="both", expand=True, padx=2, pady=2)
        
        self.lbl_bmi_title = tk.Label(frame_result, text="ИМТ: —", bg="#d4d0c8", font=("Arial", 11, "bold"), anchor="w")
        self.lbl_bmi_title.pack(fill="x", padx=15, pady=6)
        
        self.lbl_cat_title = tk.Label(frame_result, text="Категория (ВОЗ):\n—", bg="#d4d0c8", font=("Arial", 10), anchor="w", justify="left")
        self.lbl_cat_title.pack(fill="x", padx=15, pady=2)
        
        self.lbl_risk = tk.Label(frame_result, text="", bg="#d4d0c8", fg="#b22222", font=("Arial", 10, "bold"), anchor="w")
        self.lbl_risk.pack(fill="x", padx=15, pady=4)
        
        # Блок 3: Действия
        frame_actions = tk.LabelFrame(main_container, text="Действия", bg="#d4d0c8", 
                                      font=("Arial", 9, "bold"), bd=2, relief="groove")
        frame_actions.pack(fill="x", side="top", pady=6)
        
        btn_add = tk.Button(frame_actions, text="Добавить в журнал", width=18, bd=2, relief="raised", activebackground="#d4d0c8", command=self.execute_logging)
        btn_add.pack(side="left", padx=6, pady=6, expand=True, fill="x")
        
        btn_export = tk.Button(frame_actions, text="Экспорт отчёта", width=16, bd=2, relief="raised", activebackground="#d4d0c8", command=self.execute_export)
        btn_export.pack(side="left", padx=6, pady=6, expand=True, fill="x")
        
        btn_backup = tk.Button(frame_actions, text="Резервная копия журнала", width=22, bd=2, relief="raised", activebackground="#d4d0c8", command=self.execute_backup)
        btn_backup.pack(side="left", padx=6, pady=6, expand=True, fill="x")
        
        btn_refresh = tk.Button(frame_actions, text="Обновить историю", width=16, bd=2, relief="raised", activebackground="#d4d0c8", command=self.refresh_history_view)
        btn_refresh.pack(side="left", padx=6, pady=6, expand=True, fill="x")
        
        # Блок 4: Журнал измерений
        frame_journal = tk.LabelFrame(main_container, text="Журнал измерений (анонимно, UUID)", bg="#d4d0c8", 
                                      font=("Arial", 9, "bold"), bd=2, relief="groove")
        frame_journal.pack(fill="both", expand=True, side="top", pady=2)
        
        # ИСПРАВЛЕНИЕ: Вертикальный скроллбар в один серый тон Windows Classic
        v_scrollbar = tk.Scrollbar(frame_journal, bd=1, relief="raised", bg="#d4d0c8", activebackground="#d4d0c8")
        v_scrollbar.pack(side="right", fill="y")
        
        # ИСПРАВЛЕНИЕ: Добавлен горизонтальный скроллбар, чтобы текст гарантированно не уходил за рамки
        h_scrollbar = tk.Scrollbar(frame_journal, orient="horizontal", bd=1, relief="raised", bg="#d4d0c8", activebackground="#d4d0c8")
        h_scrollbar.pack(side="bottom", fill="x")
        
        self.txt_history = tk.Listbox(frame_journal, bd=2, relief="sunken", bg="white", 
                                      font=("Courier", 10), xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        self.txt_history.pack(fill="both", expand=True, padx=4, pady=4)
        
        # Связывание скроллбаров с Listbox
        v_scrollbar.config(command=self.txt_history.yview)
        h_scrollbar.config(command=self.txt_history.xview)
        
        self.lbl_status = tk.Label(self.master, text="Готово к работе", bd=1, relief="sunken", anchor="w", bg="#d4d0c8", font=("Arial", 9))
        self.lbl_status.pack(side="bottom", fill="x")

    def execute_calculation(self):
        try:
            w = float(self.entry_weight.get().replace(",", "."))
            h = float(self.entry_height.get().replace(",", "."))
            bmi, cat, risk = core.calculate_bmi(w, h)
            
            self.lbl_bmi_title.config(text=f"ИМТ: {bmi}")
            self.lbl_cat_title.config(text=f"Категория (ВОЗ):\n{cat}")
            self.lbl_risk.config(text=f"Риск для здоровья: {risk}")
            self.lbl_status.config(text="Расчет успешно выполнен.")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Введите корректные числовые параметры веса и роста.")

    def execute_clear(self):
        self.entry_weight.delete(0, tk.END)
        self.entry_height.delete(0, tk.END)
        self.lbl_bmi_title.config(text="ИМТ: —")
        self.lbl_cat_title.config(text="Категория (ВОЗ):\n—")
        self.lbl_risk.config(text="")
        self.lbl_status.config(text="Поля ввода очищены.")

    def execute_logging(self):
        try:
            w = float(self.entry_weight.get().replace(",", "."))
            h = float(self.entry_height.get().replace(",", "."))
            bmi, cat, risk = core.calculate_bmi(w, h)
            ts = core.add_to_journal(w, h, bmi, cat, risk)
            self.refresh_history_view()
            messagebox.showinfo("Журналирование", f"Лог успешно сохранен в CSV в {ts}")
        except ValueError:
            messagebox.showerror("Ошибка", "Невозможно сохранить пустые параметры.")

    def refresh_history_view(self):
        self.txt_history.delete(0, tk.END)
        records = core.get_journal_records()
        for record in records:
            self.txt_history.insert(tk.END, record)
            self.lbl_status.config(text="История логов обновлена.")
            
    def execute_backup(self):
        try:
            filename = core.create_backup()
            messagebox.showinfo("Резервное копирование", f"Архив логов успешно создан:\n{filename}")
        except Exception as e:
            messagebox.showerror("Ошибка бэкапа", str(e))
            
    def execute_export(self):
        try:
            filepath = core.export_report()
            messagebox.showinfo("Экспорт", f"Текстовый отчет сохранен:\n{filepath}")
        except Exception as e:
            messagebox.showerror("Ошибка экспорта", str(e))