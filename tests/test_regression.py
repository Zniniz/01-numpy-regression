import numpy as np
import pytest

from regression import mse


def test_mse_matches_hand_computed_value():
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.0, 2.0, 5.0])
    # errors 0, 0, 2 -> squared 0, 0, 4 -> mean 4/3
    assert np.isclose(mse(y_true, y_pred), 4.0 / 3.0)


def test_mse_rejects_mismatched_shapes():
    y_true = np.array([1.0, 2.0, 3.0])        # shape (3,)
    y_pred = np.array([[1.0], [2.0], [3.0]])  # shape (3, 1): same numbers, wrong shape
    with pytest.raises(ValueError):
        mse(y_true, y_pred)
