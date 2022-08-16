from elasticsearch import Elasticsearch
from elasticsearch import helpers


class Es(object):
    def __init__(self, host="localhost", port=9200, user_name='', password=''):
        self.es = Elasticsearch([host], http_auth=(user_name, password), port=port, use_ssl=False)

    def insert(self, index, body, index_id):
        return self.es.index(index=index, id=index_id, body=body)

    def update(self, index, index_id, body):
        return self.es.update(index=index, id=index_id, body=body)

    def delete(self, index, index_id):
        self.es.delete(index=index, id=index_id)
        pass

    def batch_data(self, index, results):

        """ 批量写入数据 """
        action = [{
                "_index": index,
                "_type": "_doc",
                "_id": data.get('review_id') or data.get('qa_id'),
                "_source": data
            } for data in results]
        helpers.bulk(self.es, action)

    def delete_index(self, index):
        self.es.indices.delete(index=index)

    def create_index(self, index, body):
        self.es.indices.create(index=index, body=body)

    def search(self, index, body, source, size=100, scroll=None):
        results = self.es.search(index=index, body=body, size=size, scroll=scroll, _source=source, request_timeout=60)
        _scroll_id = results.get('_scroll_id')
        hits = results.get('hits').get('hits')
        total = 0
        if hits:
            hits = [i.get('_source') for i in hits if i.get('_source')]
            total = results.get('hits').get('total').get('value')
        return hits, _scroll_id, total

    def scroll(self, scroll_id, scroll='5m'):
        total = 0
        try:
            results = self.es.scroll(scroll_id=scroll_id, scroll=scroll)
            scroll_id = results.get('_scroll_id')
            hits = results.get('hits').get('hits')
            if hits:
                hits = [i.get('_source') for i in hits]
                total = results.get('hits').get('total').get('value')
        except Exception as e:
            hits = "The cursor time has expired"
        return hits, scroll_id, total

    def count(self, index, body):
        results = self.es.count(index=index, body=body, request_timeout=60)
        count = results.get('count')
        return int(count)

    def get(self, index, index_id):
        return self.es.get(index=index, id=index_id, ignore=404)

    def update_by_query(self, index, body1):
        self.es.update_by_query(index=index, body=body1, request_timeout=300)