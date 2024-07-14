import numpy as np
import pandas as pd


def get_dataset(size: int) -> pd.DataFrame:
    """Generate a random dataset

    Args:
        size (int): Desired size of the dataset

    Returns:
        pd.DataFrame: Generated dataframe with random data
    """
    df = pd.DataFrame()
    df['position'] = np.random.choice(["left", "middle", "right"], size)
    df['age'] = np.random.randint(1,80, size)
    df['team'] = np.random.choice(["red", "blue", "black", "green", "yellow"], size)
    dates = pd.date_range('2020-01-01', '2024-01-01')
    df['data'] = np.random.choice(dates, size)
    df['win'] = np.random.choice(["yes", "no"], size)
    df['prob'] = np.random.uniform(0, 1, size)
    
    return df


def set_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Change types of features in a dataframe.

    Args:
        df (pd.DataFrame): Dataframe whose data type is to be changed
        
    Returns:
        pd.DataFrame: DataFrame with data type changed
    """          
    df['position'] = df['position'].astype('category')
    df['age'] = df['age'].astype('int16')
    df['team'] = df['team'].astype('category')
    df['win'] = df['win'].map({'yes': True, 'no': False})
    df['prob'] = df['prob'].astype('float16')
    
    return df   
