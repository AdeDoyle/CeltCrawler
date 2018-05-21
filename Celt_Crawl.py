"""The main Celt-Crawler function."""


from Text_Info import textinfo
from Text_Links import textlinks


def celtcrawl(url):
    links_list = textlinks(url)
    crawl_list = links_list[0]
    crawl_data = textinfo(crawl_list)
    return crawl_data


information = celtcrawl('http://celt.ucc.ie/irlpage.html')
for data in information:
    print(data)
