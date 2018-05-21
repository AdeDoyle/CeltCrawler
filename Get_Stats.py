"""Counts (Irish) texts on main page of CELT, translations, Categories, Subcategories.
   Add: subcategory per category and text per subcategory.
   Old one could get authorship known and unknown count (poorly), this can be done with a secondary stat function
   to count output from Celt_Crawl function.
   TO DO: Find out if broken links are included in 'Number of texts' by counting links in category/subcategory"""


from Site_Open import siteopen


def getstats(url):
    pagestats = []
    html = siteopen(url)
    textcount = 0
    transcount = 0
    engcount = 0
    frcount = 0
    catcount = 0
    subcatcount = 0
    breakcount = 0
    """Finds and counts texts and translations"""
    for link in html.findAll('a', href=True):
        linktext = (str(link))
        ref = link.get("href")
        brokenhref = ""
        if ref == brokenhref:
            breakcount += 1
        elif "published/G" in linktext:
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
            gtextinfo = (str(textcount) + ". " + str(linkname))
    #         print(gtextinfo)
        elif "published/T" in linktext:
            transcount += 1
            engcount += 1
            linkname = link.text
            linkname = (str(linkname))
            replaces = {"\r": "", "\n": " "}
            for item in replaces:
                if item in linkname:
                    itemcount = linkname.count(item)
                    for i in range(0, itemcount):
                        itemplace = linkname.find(item)
                        linkname = linkname[:itemplace] + replaces.get(item) + linkname[itemplace + len(item):]
            entextinfo = (str(textcount) + ". " + str(linkname))
    #         print(entextinfo)
        elif "published/F" in linktext:
            transcount += 1
            frcount += 1
            linkname = link.text
            linkname = (str(linkname))
            replaces = {"\r": "", "\n": " "}
            for item in replaces:
                if item in linkname:
                    itemcount = linkname.count(item)
                    for i in range(0, itemcount):
                        itemplace = linkname.find(item)
                        linkname = linkname[:itemplace] + replaces.get(item) + linkname[itemplace + len(item):]
            frtextinfo = (str(textcount) + ". " + str(linkname))
            # print(frtextinfo)
    """Finds and counts categories"""
    categories = []
    for category in html.find_all('h4'):
        catcount += 1
        catname = category.text
        catinfo = ("   " + str(catcount) + ". " + catname)
        categories.append(catinfo)
    """Finds and counts subcategories"""
    subcategories = []
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
            subcatinfo = ("   " + str(subcatcount) + ". " + subcatname)
            subcategories.append(subcatinfo)
    pagestats.append("Number of Texts: " + str(textcount))
    pagestats.append("Number of Translations: " + str(transcount))
    pagestats.append("   English Translations: " + str(engcount))
    pagestats.append("   French Translations: " + str(frcount))
    pagestats.append("Number of Broken Links: " + str(breakcount))
    pagestats.append("Number of Categories: " + str(catcount))
    for cat in categories:
        pagestats.append(cat)
    pagestats.append("Number of Subcategories: " + str(subcatcount))
    for subcate in subcategories:
        pagestats.append(subcate)
    return pagestats


for stat in getstats('http://celt.ucc.ie/irlpage.html'):
    print(stat)
