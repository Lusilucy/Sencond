import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.content)

        data['data']['items'][0]['quote']['name'] = "Rose"
        data['data']['items'][1]['quote']['current'] = "0.01"
        flow.response.text = json.dumps(data)
