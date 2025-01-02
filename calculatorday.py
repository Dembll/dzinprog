import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta


# Функция для добавления 115 дней к дате
def add_115_days(year, month, day):
    try:
        # Создаем объект datetime из выбранных года, месяца и дня
        date = datetime(year, month, day)
        # Добавляем 115 дней
        new_date = date + timedelta(days=115)
        return new_date.strftime("%Y-%m-%d")
    except ValueError:
        # Если введена некорректная дата
        messagebox.showerror("Ошибка", "Ошибка при вычислении даты.")
        return None


# Функция для обработки нажатия кнопки
def on_button_click():
    try:
        # Получаем значения из комбобоксов
        year = int(year_combobox.get())
        month = int(month_combobox.get())
        day = int(day_combobox.get())

        # Вычисляем новый результат с добавленными днями
        result = add_115_days(year, month, day)
        if result:
            result_label.config(text="Результат: " + result)  # Показываем результат на метке
    except ValueError:
        # Если не выбрана дата или выбраны некорректные значения
        messagebox.showerror("Ошибка", "Пожалуйста, выберите корректную дату.")


# Создание главного окна
root = tk.Tk()
root.title("Калькулятор даты")

# Создание метки для выбора даты
label = tk.Label(root, text="Выберите дату:")
label.pack(padx=10, pady=5)

# Создание фрейма для организации элементов в одну строку
frame = tk.Frame(root)
frame.pack(padx=10, pady=5)

# Создание меток и комбобоксов для года, месяца и дня
year_label = tk.Label(frame, text="Год:")
year_label.grid(row=0, column=0, padx=5)

year_combobox = ttk.Combobox(frame, values=[str(year) for year in range(1900, 2101)], width=10)
year_combobox.set("2025")  # Устанавливаем дефолтный год
year_combobox.grid(row=0, column=1, padx=5)

month_label = tk.Label(frame, text="Месяц:")
month_label.grid(row=0, column=2, padx=5)

month_combobox = ttk.Combobox(frame, values=[str(month) for month in range(1, 13)], width=5)
month_combobox.set("1")  # Устанавливаем дефолтный месяц
month_combobox.grid(row=0, column=3, padx=5)

day_label = tk.Label(frame, text="День:")
day_label.grid(row=0, column=4, padx=5)

day_combobox = ttk.Combobox(frame, values=[str(day) for day in range(1, 32)], width=5)
day_combobox.set("1")  # Устанавливаем дефолтный день
day_combobox.grid(row=0, column=5, padx=5)

# Кнопка для выполнения операции
button = tk.Button(root, text="Добавить 115 дней", command=on_button_click)
button.pack(padx=10, pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="Результат:")
result_label.pack(padx=10, pady=5)

# Запуск главного цикла приложения
root.mainloop()
