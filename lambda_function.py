import pandas as pd
import numpy as np


def lambda_handler(event, context):
    df: pd.DataFrame = pd.DataFrame(np.random.randint(0, 100, size=(8, 4)), columns=list('ABCD'))
    print(df)
