import numpy as np

def mse(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise ValueError(f"Shape mismatch: {y_true.shape} vs {y_pred.shape}")
    return np.mean(np.square(y_true - y_pred))
    