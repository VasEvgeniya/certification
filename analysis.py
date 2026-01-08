import pandas as pd

def analyze_operations(operations):
    data = []
    for op in operations:
        data.append({
            'Type': op.operation_type,
            'Category': op.product.category,
            'Quantity': op.product.quantity,
            'Total Cost': op.product.total_cost(),
        })
    df = pd.DataFrame(data)
    return df.groupby(['Category', 'Type']).sum()