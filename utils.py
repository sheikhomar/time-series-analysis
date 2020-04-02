import pandas as pd 
import numpy as np


def load_stock_prices(data_path: str = 'data/Index2018.csv'):
    df_data = pd.read_csv(data_path)
    df_data.date = pd.to_datetime(df_data.date, dayfirst=True)
    df_data.set_index('date', inplace=True)
    
    # Set the frequency to be business days
    df_data = df_data.asfreq('b')
    
    # Fill missing data
    df_data.spx = df_data.spx.fillna(method='ffill')
    df_data.ftse = df_data.ftse.fillna(method='ffill')
    df_data.dax = df_data.dax.fillna(method='ffill')
    df_data.nikkei = df_data.nikkei.fillna(method='ffill')
    return df_data

def load_sp500_data():
    df_data = load_stock_prices()
    return df_data[['spx']].copy()
    
def load_random_walk_data():
    df_rw = pd.read_csv('data/RandWalk.csv')
    df_rw.date = pd.to_datetime(df_rw.date, dayfirst=True)
    df_rw.set_index('date', inplace=True)
    df_rw = df_rw.asfreq('b')
    return df_rw

def generate_white_noise():
    df_data = load_stock_prices()
    mean_ = df_data.spx.mean()
    wn = np.random.normal(loc=df_data.spx.mean(), scale=50, size=len(df_data))
    with pd.option_context('mode.chained_assignment', None):
        df_data['wn'] = wn
    return df_data[['wn']].copy()
