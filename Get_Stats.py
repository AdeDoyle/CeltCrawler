"""Counts (Irish) texts on main page of CELT, translations, Categories, Subcategories, subcategories per category
   and lists them all.
   TO DO: text per category/subcategory."""


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
    catnames = []
    for category in html.find_all('h4'):
        catcount += 1
        catname = category.text
        catname = (str(catname))
        catnames.append(catname)
        catinfo = ("   " + str(catcount) + ". " + catname)
        categories.append(catinfo)
    """Finds and counts subcategories"""
    subcategories = []
    subcatnames = []
    for subcat in html.find_all('p'):
        subcatname = subcat.text
        subcatname = (str(subcatname))
        if "Corpus of Electronic Texts" not in subcatname:
            subcatnames.append(subcatname)
            subcatcount += 1
            replaces = {"\r": "", "\n": " "}
            for item in replaces:
                if item in subcatname:
                    itemcount = subcatname.count(item)
                    for i in range(0, itemcount):
                        itemplace = subcatname.find(item)
                        subcatname = subcatname[:itemplace] + replaces.get(item) + subcatname[itemplace + len(item):]
            subcatinfo = ("      " + str(subcatcount) + ". " + subcatname)
            subcategories.append(subcatinfo)
    """Finds and counts subcategories per category"""
    catdict = {}
    for cname in catnames:
        subcatecount = 0
        searchtext = (str(html))
        replacables = {"&": "&amp;"}
        origname = cname
        for item in replacables:
            if item in cname:
                probpos = cname.find(item)
                cname = cname[:probpos] + replacables.get(item) + cname[probpos + len(item):]
        if cname in searchtext:
            cnamepos = searchtext.find(cname)
            if origname == catnames[-1]:
                endpos = None
            elif origname != catnames[-1]:
                nextcat = (catnames.index(origname) + 1)
                nextcatname = catnames[nextcat]
                for replacable in replacables:
                    if replacable in nextcatname:
                        probpos = nextcatname.find(replacable)
                        nextcatname = nextcatname[:probpos] + \
                            replacables.get(replacable) + nextcatname[probpos + len(replacable):]
                endpos = searchtext.find(nextcatname)
        searchtext = searchtext[cnamepos:endpos]
        identifier = "<p>"
        closer = "</p>"
        pcount = searchtext.count(identifier)
        subcatchecks = []
        for i in range(0, pcount):
            beginpos = searchtext.find(identifier) + 3
            closepos = searchtext.find(closer)
            subcattext = searchtext[beginpos:closepos]
            subcatchecks.append(subcattext)
            searchtext = searchtext[:beginpos - 3] + searchtext[closepos + 4:]
        for subcatcheck in subcatchecks:
            if subcatcheck in subcatnames:
                subcatecount += 1
        catdict.update({cname: subcatecount})
    totaltcount = textcount + transcount + breakcount
    pagestats.append("Number of Texts (total): " + str(totaltcount))
    pagestats.append("Number of Texts (links working): " + str(textcount))
    pagestats.append("Number of Texts (links broken): " + str(breakcount))
    pagestats.append("Number of Translations: " + str(transcount))
    pagestats.append("   English Translations: " + str(engcount))
    pagestats.append("   French Translations: " + str(frcount))
    pagestats.append("Number of Categories: " + str(catcount))
    pagestats.append("Number of Subcategories: " + str(subcatcount))
    """Appends Categories and, where applicable, their subcategories to the output list, pagestats, in order"""
    for cat in categories:
        pagestats.append(cat)
        cattitle = (str(cat[6:]))
        if cattitle in catdict:
            removables = {"&amp;": "&"}
            for removable in removables:
                if removable in cattitle:
                    remopos = cattitle.find(removable)
                    cattitle = cattitle[:remopos] + removables.get(removable) + cattitle[remopos + len(removable):]
            catsubcats = catdict.get(cattitle)
        if catsubcats > 0:
            pagestats.append("      Subcategories: " + str(catsubcats))
            for i in range(0, catsubcats):
                pagestats.append(subcategories[i])
            for i in range(0, catsubcats):
                subcategories.remove(subcategories[0])
    return pagestats


# for stat in getstats('http://celt.ucc.ie/irlpage.html'):
#     print(stat)
