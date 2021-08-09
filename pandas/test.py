import pandas as pd
import numpy as np
import requests
from pyecharts.charts import Bar, Line, TreeMap
from pyecharts import options as opts
noc_dict = {'ROC': 'ROC',
            'ALB': '阿尔巴尼亚',
            'ALG': '阿尔及利亚',
            'AFG': '阿富汗',
            'ARG': '阿根廷',
            'UAE': '阿联酋',
            'ARU': '阿鲁巴',
            'OMA': '阿曼',
            'AZE': '阿塞拜疆',
            'EGY': '埃及',
            'ETH': '埃塞俄比亚',
            'IRL': '爱尔兰',
            'EST': '爱沙尼亚',
            'AND': '安道尔',
            'ANG': '安哥拉',
            'ANT': '安提瓜和巴布达',
            'AUT': '奥地利',
            'EOR': '奥林匹克难民代表团',
            'AUS': '澳大利亚',
            'BAR': '巴巴多斯',
            'PNG': '巴布亚新几内亚',
            'BAH': '巴哈马',
            'PAK': '巴基斯坦',
            'PAR': '巴拉圭',
            'PLE': '巴勒斯坦',
            'BRN': '巴林',
            'PAN': '巴拿马',
            'BRA': '巴西',
            'BLR': '白俄罗斯',
            'BER': '百慕大',
            'BUL': '保加利亚',
            'MKD': '北马其顿',
            'BEN': '贝宁',
            'BEL': '比利时',
            'ISL': '冰岛',
            'PUR': '波多黎各',
            'BIH': '波黑',
            'POL': '波兰',
            'BOL': '玻利维亚',
            'BIZ': '伯利兹',
            'BOT': '博茨瓦纳',
            'BHU': '不丹',
            'BUR': '布基纳法索',
            'BDI': '布隆迪',
            'GEQ': '赤道几内亚',
            'DEN': '丹麦',
            'GER': '德国',
            'TLS': '东帝汶',
            'TOG': '多哥',
            'DOM': '多米尼加',
            'DMA': '多米尼克',
            'ECU': '厄瓜多尔',
            'ERI': '厄立特里亚',
            'FRA': '法国',
            'PHI': '菲律宾',
            'FIJ': '斐济',
            'FIN': '芬兰',
            'CPV': '佛得角',
            'GAM': '冈比亚',
            'CGO': '刚果（布）',
            'COD': '刚果（金）',
            'COL': '哥伦比亚',
            'CRC': '哥斯达黎加',
            'GRN': '格林纳达',
            'GEO': '格鲁吉亚',
            'CUB': '古巴',
            'GUM': '关岛',
            'GUY': '圭亚那',
            'KAZ': '哈萨克斯坦',
            'HAI': '海地',
            'KOR': '韩国',
            'NED': '荷兰',
            'MNE': '黑山',
            'HON': '洪都拉斯',
            'KIR': '基里巴斯',
            'DJI': '吉布提',
            'KGZ': '吉尔吉斯斯坦',
            'GUI': '几内亚',
            'GBS': '几内亚比绍',
            'CAN': '加拿大',
            'GHA': '加纳',
            'GAB': '加蓬',
            'CAM': '柬埔寨',
            'CZE': '捷克',
            'ZIM': '津巴布韦',
            'CMR': '喀麦隆',
            'QAT': '卡塔尔',
            'CAY': '开曼群岛',
            'COM': '科摩罗',
            'KOS': '科索沃',
            'CIV': '科特迪瓦',
            'KUW': '科威特',
            'CRO': '克罗地亚',
            'KEN': '肯尼亚',
            'COK': '库克群岛',
            'LAT': '拉脱维亚',
            'LES': '莱索托',
            'LAO': '老挝',
            'LBN': '黎巴嫩',
            'LTU': '立陶宛',
            'LBR': '利比里亚',
            'LBA': '利比亚',
            'LIE': '列支敦士登',
            'LUX': '卢森堡',
            'RWA': '卢旺达',
            'ROU': '罗马尼亚',
            'MAD': '马达加斯加',
            'MDV': '马尔代夫',
            'MLT': '马耳他',
            'MAW': '马拉维',
            'MAS': '马来西亚',
            'MLI': '马里',
            'MHL': '马绍尔群岛',
            'MRI': '毛里求斯',
            'MTN': '毛里塔尼亚',
            'USA': '美国',
            'ASA': '美属萨摩亚',
            'ISV': '美属维尔京群岛',
            'MGL': '蒙古',
            'BAN': '孟加拉国',
            'PER': '秘鲁',
            'FSM': '密克罗尼西亚',
            'MYA': '缅甸',
            'MDA': '摩尔多瓦',
            'MAR': '摩洛哥',
            'MON': '摩纳哥',
            'MOZ': '莫桑比克',
            'MEX': '墨西哥',
            'NAM': '纳米比亚',
            'RSA': '南非',
            'SSD': '南苏丹',
            'NRU': '瑙鲁',
            'NEP': '尼泊尔',
            'NCA': '尼加拉瓜',
            'NIG': '尼日尔',
            'NGR': '尼日利亚',
            'NOR': '挪威',
            'PLW': '帕劳',
            'POR': '葡萄牙',
            'JPN': '日本',
            'SWE': '瑞典',
            'SUI': '瑞士',
            'ESA': '萨尔瓦多',
            'SAM': '萨摩亚',
            'SRB': '塞尔维亚',
            'SLE': '塞拉利昂',
            'SEN': '塞内加尔',
            'CYP': '塞浦路斯',
            'SEY': '塞舌尔',
            'KSA': '沙特阿拉伯',
            'STP': '圣多美和普林西比',
            'SKN': '圣基茨和尼维斯',
            'LCA': '圣卢西亚',
            'SMR': '圣马力诺',
            'VIN': '圣文森特和格林纳丁斯',
            'SRI': '斯里兰卡',
            'SVK': '斯洛伐克',
            'SLO': '斯洛文尼亚',
            'SWZ': '斯威士兰',
            'SUD': '苏丹',
            'SUR': '苏里南',
            'SOL': '所罗门群岛',
            'SOM': '索马里',
            'TJK': '塔吉克斯坦',
            'THA': '泰国',
            'TAN': '坦桑尼亚',
            'TGA': '汤加',
            'TTO': '特立尼达和多巴哥',
            'TUN': '突尼斯',
            'TUV': '图瓦卢',
            'TUR': '土耳其',
            'TKM': '土库曼斯坦',
            'VAN': '瓦努阿图',
            'GUA': '危地马拉',
            'VEN': '委内瑞拉',
            'BRU': '文莱',
            'UGA': '乌干达',
            'UKR': '乌克兰',
            'URU': '乌拉圭',
            'UZB': '乌兹别克斯坦',
            'ESP': '西班牙',
            'GRE': '希腊',
            'SGP': '新加坡',
            'NZL': '新西兰',
            'HUN': '匈牙利',
            'SYR': '叙利亚',
            'JAM': '牙买加',
            'ARM': '亚美尼亚',
            'YEM': '也门',
            'IRQ': '伊拉克',
            'IRI': '伊朗',
            'ISR': '以色列',
            'ITA': '意大利',
            'IND': '印度',
            'INA': '印度尼西亚',
            'GBR': '英国',
            'IVB': '英属维尔京群岛',
            'JOR': '约旦',
            'VIE': '越南',
            'ZAM': '赞比亚',
            'CHA': '乍得',
            'CHI': '智利',
            'CAF': '中非',
            'CHN': '中国',
            'HKG': '中国香港',
            'TPE': '中华台北'}
sports_dict = {'TTE': '乒乓球',
               'BDM': '羽毛球',
               'VVO': '排球',
               'VBV': '沙滩排球',
               'BKB': '篮球',
               'BK3': '三人篮球',
               'FBL': '足球',
               'TEN': '网球',
               'HBL': '手球',
               'GLF': '高尔夫',
               'RUG': '橄榄球',
               'HOC': '曲棍球',
               'BSB': '棒球',
               'DIV': '跳水',
               'SWM': '游泳',
               'SWA': '花样游泳',
               'OWS': '马拉松游泳',
               'WPO': '水球',
               'SRF': '冲浪',
               'ATH': '田径',
               'TRI': '铁人三项',
               'MPN': '现代五项',
               'GAR': '竞技体操',
               'GRY': '艺术体操',
               'GTR': '蹦床',
               'WRE': '摔跤',
               'FEN': '击剑',
               'BOX': '拳击',
               'JUD': '柔道',
               'TKW': '跆拳道',
               'KTE': '空手道',
               'CRD': '公路自行车',
               'CTR': '场地自行车',
               'MTB': '山地自行车',
               'BMF': '自由式小轮车',
               'BMX': '小轮车竞速',
               'SKB': '滑板',
               'CLB': '攀岩',
               'ROW': '赛艇',
               'CSL': '皮划艇激流回旋',
               'CSP': '皮划艇静水',
               'SAL': '帆船',
               'ARC': '射箭',
               'SHO': '射击',
               'WLF': '举重',
               'EQU': '马术'}
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
}
athlete_url = 'https://olympics.com/tokyo-2020/olympic-games/zh/results/all-sports/zzje001a.json'
data = requests.get(athlete_url,headers=headers).json()
# data =
athletes_df = pd.DataFrame(columns=['姓名', '国家', '项目'])
for item in data['data']:
    athletes_df = athletes_df.append(
        [{'姓名': item['name'], '国家':noc_dict[item['noc']], '项目':sports_dict[item['dis']]}])

athletes_df = athletes_df.reset_index(drop=True)
df_t = athletes_df.groupby(['国家', '项目'])['姓名'].count().reset_index()
df_t.columns = ['国家', '项目', '人数']

data = []
country = []
for idx, row in df_t.iterrows():
    if row['国家'] in country:
        data[-1]['children'].append(dict(name=row['项目'], value=row['人数']))
    else:
        data.append(dict(name=row['国家'], children=[dict(name=row['项目'], value=row['人数'])]))
    country.append(row['国家'])
print(data)

tree = TreeMap(
    init_opts=opts.InitOpts(
        theme='light',
        width='1000px',
        height='600px',
        # bg_color='rgb(0,0,0)'
        ))
tree.add(
    "参赛人数",
    data,
    leaf_depth=1,
    label_opts=opts.LabelOpts(position="inside", formatter='{b}：{c}名'),
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
    title_opts=opts.TitleOpts(title="2020东京奥运会参赛人数统计（国家/地区）", pos_left='center', title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)),
    legend_opts=opts.LegendOpts(is_show=False)
    )

tree.render("ay.html")