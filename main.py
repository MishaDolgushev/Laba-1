import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import generator

def show_error_message(message):
    messagebox.showerror("Ошибка", message)

def get_selected_dates():
    global start_date, end_date, advertising_time, dataset_size
    
    start_date = start_date_picker.get_date()
    end_date = end_date_picker.get_date()
    
    advertising_time_entry = ad_duration_entry.get()
    if advertising_time_entry:
        try:
            advertising_time = int(advertising_time_entry)
            if advertising_time <= 0:
                raise ValueError
        except ValueError:
            show_error_message("Неверное значение для продолжительности рекламы. Введите положительное целое число.")
            return
    else:
        advertising_time = None
    
    dataset_size_entry_value = dataset_size_entry.get()
    if dataset_size_entry_value:
        try:
            dataset_size = int(dataset_size_entry_value)
            if dataset_size <= 0:
                raise ValueError
        except ValueError:
            show_error_message("Неверное значение для размера датасета. Введите положительное целое число.")
            return
    else:
        show_error_message("Введите значение для размера датасета.")
        return
    
    root.destroy()
    

root = tk.Tk()
root.title("Выбор дат, продолжительности рекламы и размера датасета")

start_date_picker = Calendar(root, selectmode="day", date_pattern="dd/MM/yyyy")
start_date_picker.pack()

end_date_picker = Calendar(root, selectmode="day", date_pattern="dd/MM/yyyy")
end_date_picker.pack()

ad_duration_label = tk.Label(root, text="Продолжительность рекламы (в секундах на ролик):")
ad_duration_label.pack()

ad_duration_entry = tk.Entry(root)
ad_duration_entry.pack()

dataset_size_label = tk.Label(root, text="Размер датасета:")
dataset_size_label.pack()

dataset_size_entry = tk.Entry(root)
dataset_size_entry.pack()

button = tk.Button(root, text="Выбрать", command=get_selected_dates)
button.pack()

root.mainloop()

print("Файл сгенерирован")
generator.generate(int(dataset_size), start_date, end_date, advertising_time)