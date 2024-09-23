import logging
import pandas as pd


def transform_csv(csv_filename: str) -> str:
    """
    Read CSV.
    Apply transformations.
    """
    logging.info("Reading CSV")
    df = pd.read_csv(csv_filename)
    logging.info(f"{len(df)} rows in the file")

    # let's assume transformations are happening here
    return "Transformed"
