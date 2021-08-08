from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        with open("/Users/lusi/PycharmProjects/Sencond/20-23HTTP/21WorkSpace/quote.json") as f:
            flow.response = http.HTTPResponse.make(
                200,
                f.read(),
                {"Content-Type": "application/json"}
            )
