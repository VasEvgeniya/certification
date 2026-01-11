import csv  
import os
from models import Operation
from tkinter import messagebox
import pandas as pd

DATA_DIR="./data"
CSV_FILE=os.path.join(DATA_DIR,"Products.csv")

def ensure_data_dir():
    if not os.path.isfile(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_operations(operations):
    os.makedirs(DATA_DIR, exist_ok=True) 
    file_exists=os.path.isfile(CSV_FILE)
    try:

        date = operations.date_label
        operation_type = operations.operation_type
        name = operations.name
        item_type = operations.category
        quantity = operations.quantity
        price = operations.price
        calculated_value = operations.calculated_value_label

        if file_exists == True:
            df = pd.read_csv(CSV_FILE)
        else:
            df = pd.DataFrame(columns=["date", "operation_tp", "name", "item_tp", "quantity", "price", "calculated_val"])

        df.loc[len(df)] = [date, operation_type, name, item_type, quantity, price, calculated_value]
        df.to_csv(CSV_FILE, index=False)

        messagebox.showinfo("Успех", "Данные успешно сохранены!")
        

    except Exception as e:
        print(f"ОШибка при сохранении данных: {e}")


def load_operations()->pd.DataFrame:
    try:
        if os.path.isfile(CSV_FILE) == True:
            df = pd.read_csv(CSV_FILE)
        else:
            df = pd.DataFrame(columns=["date", "operation_tp", "name", "item_tp", "quantity", "price", "calculated_val"])
        return df     


    except Exception as e:
        print(f"Error loading from file: {e}")
        # return[]
    