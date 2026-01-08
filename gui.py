
import tkinter as tk
from tkinter import ttk, messagebox,Radiobutton
from models import Operation
from datetime import datetime
from storage import save_operations, load_operations  
from analysis import analyze_operations
from utiils import validate_date,validate_amount

# def calculate():
#     # """Вычисляет произведение количества и цены."""
#     try:
#         quantity = float(quantity_entry.get())
#         price = float(price_entry.get())
#         print(price)
#         result = quantity * price
#         calculated_value_label.config(text=str(result))
#     except ValueError:
#         messagebox("Ошибка ввода")


# def add_operation():
#     # quantity=q
#     # price=self.price_entry.get()
#     if not validate_amount(self.price_entry.get()):
#         messagebox("Ошибка! Некоррректная цена")
#         return
        
#     if not validate_amount(quantity_entry.get()):
#         messagebox("Ошибка! Некоррректное количество")
#         return
        
#     try:
#         op=Operation(
#             self.name_entry.get(),
#             self.category_entry.get(),
#             self.operation_type , # 'incoming' or 'outgoing'
#             self.date_entry,
#             self.comment_entry.get(),
#             self.quantity_entry,
#             self.price_entry,
#             self.total_cost_entry
#         )
            
#     except ValueError as e:
#         messagebox.showerror("Ошибка",str(e))
#         return
#     self.Operation.append(op)
#     save_operations(self.Operation)
#     messagebox.showinfo("Операция добавлена")

#     def show_operations(self):
#         # Logic for displaying operations  
#         pass

#     def analyze(self):
#         df = analyze_operations(self.operations)
#         # Visualization logic  
#         plot_pie_by_category(df,"incoming")
#         plot_pie_by_category(df,"outgoing")


class WarehouseApp:
    def __init__(self, root):
        print("1/")
        # self.root = root  
        # self.root.title("Складской учет")
        # self.operations = load_operations()


        # root = tk.Tk()

        root.title("Учет операций")

        # Дата

        date_label = tk.Label(root, text=datetime.now().strftime("%d.%m.%Y"), width=20)

        date_label.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Тип операции

        operation_var = tk.StringVar()

        operation_radio_in = tk.Radiobutton(root, text="Поступление", variable=operation_var, value="Поступление")

        operation_radio_out = tk.Radiobutton(root, text="Отпуск", variable=operation_var, value="Отпуск")

        operation_radio_in.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        operation_radio_out.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

        # Наименование

        name_label = tk.Label(root, text="Наименование:")

        name_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

        name_entry = tk.Entry(root)

        name_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Комментарий

        comment_label = tk.Label(root, text="Комментарий:")

        comment_label.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)

        comment_entry = tk.Entry(root)

        comment_entry.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Тип товара

        item_type_label = tk.Label(root, text="Тип:")

        item_type_label.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)

        item_type_combo = ttk.Combobox(root, values=["Продукты", "Товары"])

        item_type_combo.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        # Количество

        quantity_label = tk.Label(root, text="Количество:")

        quantity_label.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)

        quantity_entry = tk.Entry(root)

        quantity_entry.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

        # Цена

        price_label = tk.Label(root, text="Цена:")

        price_label.grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)

        price_entry = tk.Entry(root)

        price_entry.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)

        # Расчетное поле

        calculate_button = tk.Button(root, text="Рассчитать", command=calculate)

        calculate_button.grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)

        calculated_value_label = tk.Label(root, text="0.0")

        calculated_value_label.grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)

        # Кнопка сохранения

        save_button = tk.Button(root, text="Сохранить", command=save_data)

        save_button.grid(row=8, column=1, sticky=tk.E, padx=5, pady=5)


def save_data():

    # Получение данных из полей
    date = date_label.cget("text")

    operation_type = operation_var.get()

    name = name_entry.get()

    comment = comment_entry.get()

    item_type = item_type_combo.get()

    quantity = quantity_entry.get()

    price = price_entry.get()

    calculated_value = calculated_value_label.cget("text")

    # Проверка на заполненность обязательных полей

    if not all([operation_type, name, item_type, quantity, price]):

        messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля: Операция, Наименование, Тип, Количество, Цена.")

        return

    # Сохранение данных в CSV

    try:

        with open('data.csv', 'a', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([date, operation_type, name, comment, item_type, quantity, price, calculated_value])

        messagebox.showinfo("Успех", "Данные успешно сохранены!")

    except Exception as e:

        messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {e}")

# Функция для расчета значения

def calculate():

    try:

        quantity = float(quantity_entry.get())

        price = float(price_entry.get())

        result = quantity * price

        calculated_value_label.config(text=str(result))

    except ValueError:

        calculated_value_label.config(text="Ошибка ввода")

