import pandas as pd


def load_dataset():

    df = pd.read_csv("data/words_dataset.csv")

    print("Dataset loaded successfully")
    print("Total words:", len(df))

    return df