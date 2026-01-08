import csv  
import os
from models import Operation

DATA_DIR="data"
CSV_FILE=os.path.join(DATA_DIR,"Products")

def ensure_data_dir():
    if not os.path.isfile(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_operations(operations:list[Operation]):
    print("save")
    os.makedirs(DATA_DIR, exist_ok=True) 
    file_exists=os.path.isfile(CSV_FILE)
    print(file_exists)
    try:
        print("save1")
        with open(CSV_FILE,mode='a',newline='',encoding='utf-8') as f:
            fieldnames=['operation_type', 'Product', 'Category', 'Quantity', 'Price', 'Total_cost','DateOp', 'Comment']
            writer=csv.DictWriter(f,fieldnames=fieldnames, restval='N/A')
            print("save2")

            if not file_exists:
                writer.writeheader()
                print("save3")

            for t in operations:
                # writer.writerow(t.to_dict())
                print("save3")
    except Exception as e:
        print(f"ОШибка при сохранении данных: {e}")

# def save_operations(operations, filename='operations.csv'):
#     try:
#         with open(filename, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Type', 'Product', 'Category', 'Quantity', 'Price', 'Total_cost','Date', 'Comment'])
#             for op in operations:
#                 writer.writerow([
#                     op.operation_type,
#                     op.product.name,
#                     op.product.category,
#                     op.product.quantity,
#                     op.product.price,
#                     op.total_cost,
#                     op.date,
#                     op.comment,
#                 ])
#     except Exception as e:
#         print(f"Error saving to file: {e}")

def load_operations()->list[Operation]:
    # operations = []
    # if not os.path.exists(DATA_DIR):
    #     return operations
    print("load")
    try:
        with open(CSV_FILE, mode='r',encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        op=operations(
                        Product=row['name'], 
                        Category=row['Category'], 
                        Operation_type=row['operation_type'],
                        Date=row['Date'],
                        Quantity=int(row['Quantity']), 
                        Price=float(row['Price']),
                        Total_cost=float(row['total_cost']),
                        Comment=row['Comment'])
                    
                        operations.append(op)    
                    except ValueError as ev:
                        print("ошибка")


    except Exception as e:
        print(f"Error loading from file: {e}")
        # return[]
    return Operation