import re

def validate_date(date_str:str)->bool:
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$",date_str))

def validate_amount(amount:str)->float:
    match = re.match(r"\b(0|[1-9]\d*)(\.\d+)?\b", amount)
    if match is not None:
        # Пытаемся преобразовать в float, если есть точка, иначе в int
        return float(amount) if '.' in amount else int(amount)
    return 0.0 # Или можно вызвать исключение
