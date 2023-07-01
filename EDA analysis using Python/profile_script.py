import pandas as pd
from pandas_profiling import ProfileReport

dataset = pd.read_csv('supermarket_sales.csv')
prof = ProfileReport(dataset)
prof