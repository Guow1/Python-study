### elasticsearch 分页

1. form+size 浅分页

    一般要求结果数量少时使用, 可以指定起始点,灵活分页(page)常用到。但size特别大时(默认10000), 会无法查询后续结果。

2. scroll 深分页
    
    首次查询时, 会创建一个历史快照(设定过期时间),以及记录当前的终止位置, 下次查询根据终止位置查询后续数据。 
不好用,不够灵活,到期会失效, 数据更新也不会有变化。(适用于大量数据导出或者索引重建)

3. search_after 深分页 
   
   指定排序方式得到唯一排序结果,根据sort的值进行不断深入, 直至全部, query和sort字段修改会对结果有影响。

首次条件查询后结果中的sort放入search_after即可。
```json
{
  "sort": [{"term.keyword": {"order": "asc"}}],
  "query": {"bool": {"filter": [{"match_all": {}}]}},
  "size": 10,
  "search_after": ["search_after"]}
```

