"""Utility functions to handle files."""

from os import PathLike
from typing import Any, Union

import joblib


def load_object(file_path: Union[str, bytes, "PathLike[str]"]) -> Any:
    """Deserialise a Python object.

    Args:
        file_path (Union[str, bytes, "PathLike[str]"]): a path to a file to be
            written.

    Returns:
        A Python object.
    """
    return joblib.load(file_path)
