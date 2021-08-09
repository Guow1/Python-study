import pandas as pd
from pyecharts.charts import Bar, Line, TreeMap
from pyecharts import options as opts

es = pd.read_csv('./exercise_data/Euro2012_stats.csv')
print(es['Team'].nunique())