import datetime

class Operation:
    def __init__(self,
        operation_type: str,
        date_label:str,
        category: str,
        name: str,
        calculated_value_label:float,
        quantity:float=0, 
        price:float=0
   ):
    
        # operation_type="incoming"
        # quantity_new=0
        # if operation_type not in ("incoming","outgoing"):
        #     raise ValueError("Тип операции может быть incoming или outgoing")
        # print(quantity_label.get())

        # if int(quantity_label.get()) > 0:
        #     if operation_type=="incoming":
        #         quantity_new=self.quantity+quantity
        #     else:    
        #         if quantity <= self.quantity:
        #             quantity_new=self.quantity-quantity
        #         else:
        #             raise ValueError(f"Недостаточно количества  {self.name}")
        # elif quantity < 0:
        #     raise ValueError("Количество может быть только положительное")
        # else:
        #     raise ValueError("Количество не может быть равно 0")
        # if price <=0:
        #     raise ValueError("Цена может быть только положительная")

        self.name = name
        print(self.name)
        self.category=category
        self.operation_type = operation_type  # 'incoming' or 'outgoing'
        self.date_label = date_label
        self.quantity=quantity
        self.price = price
        self.calculated_value_label = calculated_value_label

        self.oper_dict = {"name":name, "category":category, "operation_type":operation_type, "date_label":date_label, 
                          "quantity":quantity, "price":price, "calculated_value_label":calculated_value_label}
        
        self.oper_arr = [name, category, operation_type, date_label, quantity, price, calculated_value_label]

    @staticmethod
    def _validate_date(date_str:str)->str:
        try:
            datetime.datetime.strftime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Допустимый формат даты ГГГГ-ММ-ДД")

    def _to_dict(self):
        return{
            'name':self.name_entry,
            'category': self.item_type_combo,
            'operation_type': self.operation_type,
            'date_label': self.date_label,
            'quantity': self.quantity_entry,
            'price': self.price_entry,
            'calculated_value_label': self.calculated_value_label
            }  
  