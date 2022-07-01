"""Data handling functions."""

import logging
from tempfile import TemporaryDirectory

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi


def get_data(
    dataset: str,
    filename: str,
) -> pd.DataFrame:
    """Ping Kaggle's API to get file from competition.

    Args:
        dataset (str): the string identified of the dataset.
        filename (str): the name of the file to be retrieved and
        converted into a pandas DataFrame.
    """
    api = KaggleApi()
    api.authenticate()
    with TemporaryDirectory() as temp_dir:
        api.dataset_download_file(dataset, filename, path=temp_dir)
        logging.info("downloaded {filename} from {competition}")
        try:
            return pd.read_csv(f"{temp_dir}/{filename}.zip")
        except FileNotFoundError:
            return pd.read_csv(f"{temp_dir}/{filename}")
