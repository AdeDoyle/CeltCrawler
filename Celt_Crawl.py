"""The main Celt-Crawler function."""


from Text_Info import textinfo
from Text_Links import textlinks
from Get_Stats import getstats


def celtcrawl(url):
    links_list = textlinks(url)
    crawl_list = links_list[0]
    crawl_data = textinfo(crawl_list)
    return crawl_data


def getmorestats(crawldata):
    outstats = []
    authcount = 0
    authors = []
    authknowncount = 0
    knownauthtexts = []
    authunknowncount = 0
    unknownauthtexts = []
    oicount = 0
    micount = 0
    emicount = 0
    oitexts = []
    mitexts = []
    emitexts = []
    irishonlycount = 0
    irishonlytexts = []
    otherlangcount = 0
    otherlangs = []
    for entry in crawldata:
        entname = entry[1]
        entname = entname[6:]
        authdata = entry[2]
        if authdata == "Author: Unknown":
            authunknowncount += 1
            unknownauthtexts.append(entname)
        else:
            authknowncount += 1
            knownauthtexts.append(entname)
            authname = authdata[8:]
            if authname not in authors:
                authcount += 1
                authors.append(authname)
        irformdata = entry[3]
        if "Old Irish" in irformdata:
            oicount += 1
            oitexts.append(entname)
        if "Middle Irish" in irformdata:
            micount += 1
            mitexts.append(entname)
        if "Early Modern Irish" in irformdata:
            emicount += 1
            emitexts.append(entname)
        otherlangdata = entry[4]
        if otherlangdata == "None":
            irishonlycount += 1
            irishonlytexts.append(entname)
        else:
            for langtag in otherlangdata:
                if langtag not in otherlangs:
                    otherlangcount += 1
                    otherlangs.append(langtag)
    outstats.append("Number of Authors: " + str(authcount))
    outstats.append("Number of Texts (author known): " + str(authknowncount))
    outstats.append("Number of Texts (author unknown): " + str(authunknowncount))
    outstats.append("Number of Texts (Old Irish): " + str(oicount))
    outstats.append("Number of Texts (Middle Irish): " + str(micount))
    outstats.append("Number of Texts (Early Modern Irish): " + str(emicount))
    outstats.append("Number of Texts (Irish Only): " + str(irishonlycount))
    outstats.append("Number of Alternative Languages: " + str(otherlangcount))
    # print(authors)
    # print(knownauthtexts)
    # print(unknownauthtexts)
    # print(oitexts)
    # print(mitexts)
    # print(emitexts)
    # print(irishonlytexts)
    # print(otherlangs)
    # return authors
    # return knownauthtexts
    # return unknownauthtexts
    # return oitexts
    # return mitexts
    # return emitexts
    # return irishonlytexts
    # return otherlangs
    return outstats


for stat in getstats('http://celt.ucc.ie/irlpage.html'):
    print(stat)

information = celtcrawl('http://celt.ucc.ie/irlpage.html')
# for data in information:
#     print(data)

for stat in getmorestats(information):
    print(stat)
