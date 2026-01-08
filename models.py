import datetime

class Operation:
    def __init__(
        name: str = "",
        category: str = "Food", #Tools
        operation_type: str = "incoming"
        ):
    
        if operation_type not in ("incoming","outgoing"):
            raise ValueError("Тип операции может быть incoming или outgoing")

        if quantity > 0:
            if operation_type=="incoming":
                self.quantity=self.quantity+quantity
            else:    
                if quantity <= self.quantity:
                    self.quantity=self.quantity-quantity
                else:
                    raise ValueError(f"Недостаточно количества  {self.name}")
        elif quantity < 0:
            raise ValueError("Количество может быть только положительное")
        else:
            raise ValueError("Количество не может быть равно 0")
        if price <=0:
            raise ValueError("Цена может быть только положительная")

        self.name = name.strip()
        print(self.name)
        self.category=category.strip()
        self.operation_type = operation_type.strip()  # 'incoming' or 'outgoing'
        self.date = self._validate_date(date)
        self.comment = comment.strip()
        self.price = price
        self.total_cost = self.quantity * self.price

    @staticmethod
    def _validate_date(date_str:str)->str:
        try:
            datetime.datetime.strftime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Допустимый формат даты ГГГГ-ММ-ДД")

    def _to_dict(self):
        return{
            'name':self.name,
            'category': self.category,
            'operation_type': self.operation_type,
            'date': self.date,
            'quantity': self.quantity,
            'price': self.price,
            'total_cost': self.total_cost,
            'comment': self.comment
        }