# 01 - import modules
import pandas as pd
import numpy as np

# adjust default settings
pd.options.display.max_columns = 60
pd.options.display.max_rows = 35
import warnings
warnings.filterwarnings("ignore")

# import libraries
# source: https://github.com/duarteocarmo/interactive-dashboard-post
import requests
import textblob
import plotly.express as px
pd.set_option('display.max_colwidth', -1) # don't cut my pandas dataframes
