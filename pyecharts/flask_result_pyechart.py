# !/usr/bin/python3
# encoding:utf-8
import requests
import configparser
from flask import Flask, jsonify, send_from_directory, make_response
from flask_restful import reqparse, Api, Resource, abort
from loguru import logger
from pyecharts.charts import Bar, Line
from pyecharts import options as opts
from markupsafe import Markup

app = Flask(__name__, static_folder="templates")
app.config['JSON_SORT_KEYS'] = False
app.config['ERROR_404_HELP'] = False

api = Api(app, errors=app.errorhandler)


def api_abort(http_status_code, status_code, message):
    response = make_response(jsonify({"status": status_code, "error_message": message}), http_status_code)
    abort(response)


@app.errorhandler(Exception)
def exception_handler(e):
    resp_body = {"status": -1, "cookie": [], "error_message": str(e)[:300]}
    logger.error(f"服务端返回错误结果 -> {resp_body}")
    return jsonify(resp_body)


@app.route('/<path:path>')
def serve_page(path):
    return send_from_directory('docs', path)


class Amazon_asin(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('item', required=False, action="store", type=str, location='args', default='1',
                            nullable=True)
        args = parser.parse_args()
        item = args.get('item')
        # logger.info(item)
        # dt = requests.get(
        # f"http://192.168.10.62:5000/api/stock?item={item}&start_date=2021-08-1&end_date=2021-08-05").json()
        dt = {'status': 200, 'item_id': '723262677', 'results': [{'Biblestore': [{'date': ['2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [0, 0, 0, 0], 'price': ['$17.0', '$17.0', '$11.43', '$17.0', '$17.0'], 'quantity': [1, 1, 1, 1, 1]}]}, {'Walmart.com': [{'date': ['2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-05'], 'sales': [0, 16, 15, 9, 5, 12, 0, 0], 'price': ['$10.36', '$10.36', '$10.36', '$10.38', '$10.38', '$10.38', '$10.38', '$10.38', '$10.38'], 'quantity': [969, 1005, 989, 974, 965, 960, 948, 976, 547]}]}, {'Book Outlet': [{'date': ['2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [0, 0, 0, 0, 1, 0, 0, 0, 0], 'price': ['$6.25', '$6.25', '$6.25', '$6.25', '$6.25', '$6.25', '$6.25', '$6.25', '$6.25', '$6.25'], 'quantity': [50, 50, 50, 50, 50, 49, 50, 50, 50, 50]}]}, {'Bible Mega Mall': [{'date': ['2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [8, 3, 13, 11, 15, 0, 0, 23, 6], 'price': ['$14.11', '$14.11', '$14.11', '$14.11', '$14.11', '$14.11', '$14.11', '$14.11', '$14.11', '$14.11'], 'quantity': [465, 457, 454, 441, 430, 415, 415, 445, 422, 416]}]}, {'Fishpond Inc': [{'date': ['2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [0, 0, 0, 0, 0, 0, 0, 0], 'price': ['$18.47', '$19.04', '$19.04', '$19.04', '$16.58', '$16.58', '$15.06', '$15.06', '$15.06'], 'quantity': [1, 1, 1, 1, 1, 1, 1, 1, 1]}]}, {'Grand Eagle Retail': [{'date': ['2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [17, 0, 0, 0, 0, 0, 0, 0, 0], 'price': ['$20.37', '$17.49', '$17.49', '$17.49', '$17.49', '$17.49', '$17.49', '$17.49', '$17.49', '$17.49'], 'quantity': [20, 3, 3, 3, 3, 3, 3, 3, 3, 3]}]}, {'BooksXpress': [{'date': ['2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'price': ['$13.96', '$13.96', '$13.96', '$13.96', '$13.96', '$13.96', '$13.96', '$13.96', '$13.96', '$13.96'], 'quantity': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]}]}, {'Rocky Mountain Textbooks': [{'date': ['2021-08-04', '2021-08-05'], 'sales': [0], 'price': ['$23.95', '$23.95'], 'quantity': [1, 1]}]}, {'Saanjhi Inc.': [{'date': ['2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31', '2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05'], 'sales': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'price': ['$17.63', '$17.63', '$17.63', '$17.63', '$17.63', '$17.63', '$17.63', '$17.63', '$17.63', '$17.63'], 'quantity': [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]}]}]}

        results = dt.get("results")
        c = (
            Bar(init_opts=opts.InitOpts(width="1540px", height="720px"))
                .add_xaxis(["2021-08-01", "2021-08-02", '2021-08-03', '2021-08-04', '2021-08-05'])
                .set_global_opts(title_opts=opts.TitleOpts(title="商品库存变化", subtitle="gw"))
        )
        if results:
            for seller in results:
                seller_name = [i for i in seller.keys()][0]
                quantity = [j[0].get("quantity") for j in seller.values()][0]
                date = [j[0].get("date") for j in seller.values()][0]
                c.add_yaxis(seller_name, quantity)
        resp = self.out_html(Markup(c.render_embed()), 200)
        return resp

    @api.representation("text/html")
    def out_html(self, data, code, headers=None):
        resp = make_response(data, code)
        resp.headers.extend(headers or {})
        return resp


api.add_resource(Amazon_asin, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
