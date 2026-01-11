import tkinter as tk  
from gui import WarehouseApp
from storage import save_operations, load_operations
from typing import Dict, Any


# warehouse_app/
# │  
# ├── main.py             # Основной файл для запуска приложения  
# ├── models.py           # Определение классов для финансовых операций и товаров  
# ├── storage.py          # Работа с файлами (чтение/запись CSV)
# ├── analysis.py         # Функции для анализа данных  
# ├── gui.py              # Графический интерфейс  
# ├── requirements.txt    # Список зависимостей  
# └── tests.py            # Unit-тесты

# Main execution  
if __name__ == "__main__":
    # main()
    root = tk.Tk()
    app = WarehouseApp(root)
    root.mainloop()