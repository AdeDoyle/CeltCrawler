"""Finds the href for each link on a page"""

from Site_Open import siteopen
from Site_Text import sitetext


def findrefs(url):
    reflist = []
    html = siteopen(url)
    """opens all links on irish text page"""
    for link in html.findAll('a', href=True):
        ref = link.get('href')
        """Fixes broken links where href entered without = sign"""
        if ref == "":
            title = link.text
            if "á" in title:
                for letter in title:
                    if letter == "á":
                        fadaplace = title.find("á")
                        title = title[:fadaplace] + "&aacute;" + title[fadaplace + 1:]
            titlelength = len(title)
            rawsite = sitetext(url)
            titleplace = rawsite.find(title)
            searchstring = rawsite[:titleplace + titlelength]
            startoflink = searchstring.rfind('href"') + 5
            endoflink = searchstring.rfind(".html") + 5
            ref = searchstring[startoflink:endoflink]
        reflist.append(ref)
    return reflist


# checklist = findrefs('http://celt.ucc.ie/irlpage.html')
# count = 0
# for item in checklist[138:146]:
#     count += 1
#     print(str(count) + ": " + item)
