import numpy as np

def calculate(numbers):
    """Return column, row, and overall statistics for nine numbers."""
    if len(numbers) != 9:
        raise ValueError('List must contain nine numbers.')

    matrix = np.array(numbers).reshape(3, 3)
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }
    calculations = {
        name: [
            operation(matrix, axis=0).tolist(),
            operation(matrix, axis=1).tolist(),
            operation(matrix).item(),
        ]
        for name, operation in operations.items()
    }
    return calculations
