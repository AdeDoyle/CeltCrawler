"""Opens the web page entered and returns parsed HTML code."""

import requests


def sitetext(url):
    web_source = url
    source_code = requests.get(web_source)
    plain_text = source_code.text
    return plain_text


# print(sitetext('http://celt.ucc.ie/irlpage.html'))
