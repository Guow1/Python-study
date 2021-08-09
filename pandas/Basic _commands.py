import pandas as pd
import numpy as np

"""
本节主要包含pandas的基础命令
"""
# 数据的导入
filename, query, connection_object, json_string, url, table_name, df, n = '', '', '', '', '', '', '', 8
pd.read_csv(filename)  # 导入csv格式文件中的数据
pd.read_table(filename)  # 导入有分隔符的文本 (如TSV) 中的数据
pd.read_excel(filename)  # 导入Excel格式文件中的数据
pd.read_sql(query, connection_object)  # 导入SQL数据表/数据库中的数据
pd.read_json(json_string)  # 导入JSON格式的字符，URL地址或者文件中的数据
pd.read_html(url)  # 导入经过解析的URL地址中包含的数据框 (DataFrame) 数据
pd.read_clipboard()  # 导入系统粘贴板里面的数据
pd.DataFrame(dict)  # 导入Python字典 (dict) 里面的数据，其中key是数据框的表头，value是数据框的内容。
# 数据导出
ch = pd.DataFrame(np.random.rand(10, 5))  # 创建一个5列10行的由随机浮点数组成的数据框 DataFrame
ch.to_csv(filename)  # 将数据框 (DataFrame)中的数据导入csv格式的文件中
ch.to_excel(filename)  # 将数据框 (DataFrame)中的数据导入Excel格式的文件中
ch.to_sql(table_name, connection_object)  # 将数据框 (DataFrame)中的数据导入SQL数据表/数据库中
ch.to_json(filename)  # 将数据框 (DataFrame)中的数据导入JSON格式的文件中
# 数据创建
ch1 = pd.DataFrame(np.random.randint(5, size=(10, 5)))
my_list = ['Kesci', 100, '欢迎来到科赛网']
pd.Series(my_list)  # 从一个可迭代的对象 my_list 中创建一个数据组
ch1.index = pd.date_range('2017/1/1', periods=ch1.shape[0])  # 添加一个日期索引 index
ch1.head(n)  # 查看数据框的前n行
ch1.tail(n)  # 查看数据框的最后n行
a = ch1.shape  # 查看数据框的行数与列数
ch1.info()  # 查看数据框 (DataFrame) 的索引、数据类型及内存信息
ch1.describe()  # 对于数据类型为数值型的列，查询其描述性统计的内容
ch1.value_counts(dropna=False)  # 查询单独列独特数据值出现次数统计
ch1.apply(pd.Series.value_counts)  # 查询数据框 (Data Frame) 中每个列的独特数据值出现次数统计
b = ch1[2]  # 以数组 Series 的形式返回选取的列
c = ch1[[2, 3]]  # 以新的数据框(DataFrame)的形式返回选取的列
aa = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))
bb, cc = aa.iloc[2, :], aa.iloc[2, 2]  # 读取行以及特定位置元素
ch1['item_name'].nunique()
