import pandas as pd
from pyecharts.charts import Bar, Line, TreeMap
from pyecharts import options as opts

"""
要求: 展示销量前五的item_name(包含数量),同时展示销量前五中描述的前五(包含数量),图表表示关系
过程: 使用矩形树图
"""

path = "./exercise_data/chipotle.tsv"
chipo = pd.read_csv(path, header=0, sep='\t')
# chipo['quantity'].sum()  quantity总数
# chipo['choice_description'].value_counts().head()
# print(chipo['item_name'].nunique()) 在item_name这一列中，一共有多少种商品被下单
# print(chipo['choice_description'].value_counts().head())  在choice_description中，下单次数最多的商品是什么？
# print(chipo.head(10)) 打印的前10行数据
# chipo.shape[1] 打印的列的数量
# print(chipo.columns) 打印出全部的列名称
# print(chipo.index)  数据集的索引,步进
# print(d['item_name'].nunique())  查询item_name的个数
# d['item_name'].unique()  打印item_name
c = chipo[['item_name', 'quantity']].groupby(['item_name'], as_index=False).agg({'quantity': sum})
c.sort_values(['quantity'], ascending=False, inplace=True)
d = chipo[['item_name', 'choice_description', 'quantity']]
ss = {}
for i in d['item_name'].unique():
    a = d.loc[d['item_name'] == i]
    aa = a[['choice_description', 'quantity']].groupby(['choice_description'], as_index=False).agg({'quantity': sum})
    aa.sort_values(['quantity'], ascending=False, inplace=True)
    ss[i] = [{'name': row['choice_description'], 'children': [], 'value': row['quantity']} for index, row in
             aa.head(5).iterrows()]
tree = TreeMap(init_opts=opts.InitOpts(theme='light', width='1520px', height='700px'))
item_name = [{"name": row['item_name'], 'children': ss.get(row['item_name']), "value": row['quantity']} for index, row
             in c.head(10).iterrows()]
tree.add(
    "售出数量",
    item_name,
    leaf_depth=1,
    # label_opts=opts.LabelOpts(position="inside", formatter='{b}：{c}名'),
    levels=[
        opts.TreeMapLevelsOpts(
            treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                border_color="#555", border_width=4, gap_width=4
            )
        ),
        opts.TreeMapLevelsOpts(
            color_saturation=[0.3, 0.6],
            treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                border_color_saturation=0.7, gap_width=2, border_width=2
            ),
        ),
        opts.TreeMapLevelsOpts(
            color_saturation=[0.3, 0.5],
            treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                border_color_saturation=0.6, gap_width=1
            ),
        ),
        # opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
    ],
)
tree.set_global_opts(
    title_opts=opts.TitleOpts(title="商品售出数量", pos_left='center',
                              title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)),
    legend_opts=opts.LegendOpts(is_show=False)
)

tree.render("1.html")
