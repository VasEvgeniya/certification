import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def analyze_operations(operations):
    
    # Загрузка данных из CSV файла
    DATA_DIR="./data"
    CSV_FILE=os.path.join(DATA_DIR,"Products.csv")
    df = pd.read_csv(CSV_FILE)

    #     df = pd.DataFrame(columns=["date", "operation_tp", "name", "item_tp", "quantity", "price", "calculated_val"])
    # # Извлечение данных
    labels = df['operation_tp'].tolist()
    sizes = df['quantity'].tolist()

    # Построение круговой диаграммы
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # Добавление заголовка
    plt.title('Распределение по категориям')

    # Отображение диаграммы
    plt.axis('equal')  # Убедиться, что круговая диаграмма строится как круг
    plt.show()
