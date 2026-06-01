from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = ROOT_DIR / "data" / "processed"

def load_customer_data():

    customer_df = pd.read_csv(
        DATA_DIR / "customer_segments.csv"
    )

    cluster_df = pd.read_csv(
        DATA_DIR / "cluster_profiles.csv"
    )

    return customer_df, cluster_df