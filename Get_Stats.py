"""Counts texts on main page of CELT, Categories, Subcategories.
   Add: texts per category and subcategory, and count of translations"""


from Site_Open import siteopen


def getstats(url):
    pagestats = []
    html = siteopen(url)
    textcount = 0
    catcount = 0
    subcatcount = 0
    for link in html.findAll('a', href=True):
        linktext = (str(link))
        if "published/G" in linktext:
            textcount += 1
            linkname = link.text
            linkname = (str(linkname))
            replaces = {"\r": "", "\n": " "}
            for item in replaces:
                if item in linkname:
                    itemcount = linkname.count(item)
                    for i in range(0, itemcount):
                        itemplace = linkname.find(item)
                        linkname = linkname[:itemplace] + replaces.get(item) + linkname[itemplace + len(item):]
            textinfo = (str(textcount) + ". " + str(linkname))
    #         print(textinfo)
    print("")
    print("Categories:")
    for category in html.find_all('h4'):
        catcount += 1
        catname = category.text
        catinfo = (str(catcount) + ". " + catname)
        print(catinfo)
    print("")
    print("Subcategories:")
    for subcat in html.find_all('p'):
        subcatname = subcat.text
        subcatname = (str(subcatname))
        if "Corpus of Electronic Texts" not in subcatname:
            subcatcount += 1
            replaces = {"\r": "", "\n": " "}
            for item in replaces:
                if item in subcatname:
                    itemcount = subcatname.count(item)
                    for i in range(0, itemcount):
                        itemplace = subcatname.find(item)
                        subcatname = subcatname[:itemplace] + replaces.get(item) + subcatname[itemplace + len(item):]
            subcatinfo = (str(subcatcount) + ". " + subcatname)
            print(subcatinfo)
    print("")
    pagestats.append("Number of texts: " + str(textcount))
    pagestats.append("Number of categories: " + str(catcount))
    pagestats.append("Number of subcategories: " + str(subcatcount))
    return pagestats


for stat in getstats('http://celt.ucc.ie/irlpage.html'):
    print(stat)
