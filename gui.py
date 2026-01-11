import os
import tkinter as tk
from tkinter import ttk, messagebox,Radiobutton
from models import Operation
from datetime import datetime
from storage import save_operations, load_operations  
from analysis import analyze_operations
from utiils import validate_date,validate_amount
import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class WarehouseApp:

    def __init__(self, root):
        self.root = root  
        self.root.title("Складской учет")
        self.data = load_operations()

       # Дата

        self.date_label = tk.Label(root, text=datetime.now().strftime("%d.%m.%Y"), width=20)

        self.date_label.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Тип операции
        self.operation_type = tk.StringVar()
        self.operation_type.set("Поступление")

        self.operation_radio_in = tk.Radiobutton(root, text="Поступление", variable=self.operation_type, value="Поступление")

        self.operation_radio_out = tk.Radiobutton(root, text="Отпуск", variable=self.operation_type, value="Отпуск")

        self.operation_radio_in.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.operation_radio_out.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

        # Наименование

        self.name_label = tk.Label(root, text="Наименование:")

        self.name_label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

        self.name_entry = tk.Entry(root)

        self.name_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

 
        # Тип товара

        self.item_type_label = tk.Label(root, text="Тип:")

        self.item_type_label.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)

        self.item_type_combo = ttk.Combobox(root, values=["Продукты", "Товары"])

        self.item_type_combo.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        # Количество

        self.quantity_label = tk.Label(root, text="Количество:")

        self.quantity_label.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)

        # global quantity_entry_0
        
        self.quantity_entry=tk.Entry(root)   
        quantity_entry_0 = float(self.quantity_entry.get()) if self.quantity_entry.get() != '' else 0.0

        self.quantity_entry.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

        # Цена

        self.price_label = tk.Label(root, text="Цена:")

        self.price_label.grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)

        # global price_entry_0
        self.price_entry = tk.Entry(root)
        price_entry_0 = float(self.price_entry.get()) if self.price_entry.get() != '' else 0.0
    
        self.price_entry.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)



        def calculate():
            try:
                quantity = validate_amount(self.quantity_entry.get()) if self.quantity_entry.get() != '' else 0.0
                price = validate_amount(self.price_entry.get()) if self.price_entry.get() != '' else 0.0
                result = quantity * price
 
                self.calculated_value_label = tk.Label(root, text=str(result))
                self.calculated_value_label.grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)

            except ValueError:

                calculated_value_label_0.config(text="Ошибка ввода")

        

      # Расчетное поле

        calculate_button = tk.Button(root, text="Рассчитать", command=calculate)

        calculate_button.grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)

        # global calculated_value_label_0
        self.calculated_value_label = tk.Label(root, text="0.0")
        calculated_value_label_0 = self.calculated_value_label
        self.calculated_value_label.grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)


        def add_operation():
            print("Start saving...")
            try:
                op=Operation(
                    str(self.operation_type.get()) , # 'incoming' or 'outgoing'
                    str(self.date_label.cget("text")),
                    str(self.item_type_combo.get()),
                    str(self.name_entry.get()),
                    str(self.calculated_value_label.cget("text")),
                    str(self.quantity_entry.get()),
                    str(self.price_entry.get())
                )
                 
            except ValueError as e:
                messagebox.showerror("Ошибка",str(e))
                return
            
            df = self.data

            df["quantity"] = df["quantity"].astype(int)
            found = df.index[(df["name"] == self.name_entry.get()) & (df["item_tp"] == self.item_type_combo.get())].tolist()
            # print("Found:", found)
            # print("N", str(self.name_entry.get()))
            # print("name", self.name_entry, "type", self.item_type_combo)
            if len(found) == 1:
                index = found[0]

                if self.item_type_combo.get() == "Отпуск":
                    if int(df["quantity"][index]) >= int(self.quantity_entry.get()):
                        df["quantity"][index] -= int(self.quantity_entry.get())
                    else: raise ValueError(f"Недостаточно количества  {self.name.get()}")
                elif self.item_type_combo.get() == "Поступление":
                    df["quantity"][index] += int(self.quantity_entry.get())

            DATA_DIR="./data"
            CSV_FILE=os.path.join(DATA_DIR,"Products.csv")
            df.to_csv(CSV_FILE, index=False )

            # self.Operation.append(op)
            save_operations(op)
            messagebox.showinfo("Операция добавлена")


        def export_to_excel():
            DATA_DIR="./data"
            Excel_FILE=os.path.join(DATA_DIR,"Products.xlsx")
            # file_name = 'Products.xlsx'
            df = self.data
            try:
                # index=False, чтобы не записывать индекс DataFrame в файл
                df.to_excel(Excel_FILE, index=False)
                print(f"Данные успешно экспортированы в {Excel_FILE}")
            except Exception as e:
                print(f"Ошибка при экспорте: {e}")
 
        def analyze():
            df = analyze_operations(self.data)

        def analyze_prod_():
            df = analyze_prod(self.data)
      
       
        save_button = tk.Button(root, text="Добавить запись", command=add_operation)
        save_button.grid(row=8, column=1, sticky=tk.E, padx=5, pady=5)

        export_to_excel = tk.Button(root, text="Экспорт в Excel", command=export_to_excel)
        export_to_excel.grid(row=10, column=1, sticky=tk.E, padx=5, pady=5)

        analyze_button = tk.Button(root, text="Анализ по типу операции", command=analyze)
        analyze_button.grid(row=12, column=1, sticky=tk.E, padx=5, pady=5)
   
