### elasticsearch 建议器 completion suggester

[参考]: [https://www.cnblogs.com/Neeo/articles/10695019.html]

mapping创建示例 (fields增加suggest即可,详细参考资料)
```json
{
  "mappings": {
    "_doc": {
      "properties": {
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            },
            "suggest": {
              "type": "completion",
              "analyzer": "keyword",
              "preserve_separators": true,
              "preserve_position_increments": true,
              "max_input_length": 50
            }
          }
        }
      }
    }
  }
}

```
body查询示例
```json
{"suggest": {"suggestion": {"text": "a", "completion": {
            "field": "name.suggest", "size": 10}}}, 
  "_source": "name"}
```