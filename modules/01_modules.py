# 01 - import modules
# Pandas modules for working with DataFrames
import pandas as pd

# Modules for data manipulation
import numpy as np

# Modules for statistical models
import scipy
from scipy import stats
import statsmodels.api as sm

# Numpy modules for data visualization
import matplotlib.pyplot as plt

# Adjust plot settings to output correctly
%matplotlib inline

# Seaborn module for plots; built on Matplotlib package:
# https://seaborn.pydata.org/
import seaborn as sns; sns.set(color_codes=True)

# Set numeric output; turn off scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# adjust default settings
pd.options.display.max_columns = 60
pd.options.display.max_rows = 35
import warnings
warnings.filterwarnings("ignore")

# import libraries
# source: https://github.com/duarteocarmo/interactive-dashboard-post
import requests
# import textblob
import plotly.express as px
pd.set_option('display.max_colwidth', -1) # don't cut my pandas dataframes
