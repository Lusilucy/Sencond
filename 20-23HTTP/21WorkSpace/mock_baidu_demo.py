from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == 'https://www.baidu.com/':
        flow.response = http.HTTPResponse.make(
            200,
            b"Hello World",
            {"Content-Type": "text/html"}
        )
