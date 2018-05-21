"""Opens links in a list and retrieves information (Title, Author, Irish Form(s), Other Languages, Text-Link)"""


# from Text_Links import textlinks
from Site_Open import siteopen


def textinfo(urllist):
    textsinfo = []
    no_baselink = []
    infotag = "/header.html"
    maintag = ".html"
    basetag = "/index.html"
    for link in urllist:
        textdata = []
        baselink = link
        endroot = link.find(basetag)
        linkroot = link[:endroot]
        """Finds any base links which do not conform to the expected format"""
        if basetag not in baselink:
            no_baselink.append(baselink)
        else:
            infolink = linkroot + infotag
            mainlink = linkroot + maintag
            textdata.append(mainlink)
        """Opens text's header page. Finds the text name and edits it to remove html code and other issues found"""
        infohtml = siteopen(infolink)
        for title in infohtml.findAll("h1"):
            textstring = (str(title))
            textname = textstring[19:-5]
            changeables = {"f�n": "fün"}
            for item in changeables:
                if item in textname:
                    itemplace = textname.find(item)
                    textname = textname[:itemplace] + changeables.get(item) + textname[itemplace + len(item):]
            removables = ["<u>", "</u>", "\n"]
            for item in removables:
                if item in textname:
                    itemcount = textname.count(item)
                    for i in range(0, itemcount):
                        itemplace = textname.find(item)
                        textname = textname[:itemplace] + textname[itemplace + len(item):]
            textnamedata = "Text: " + textname
            textdata.append(textnamedata)
        """Finds the author's name, where given, and removes any issues found"""
        authunknowns = ["unknown", "Unknown", "[unknown]"]
        for author in infohtml.findAll("h2"):
            authstring = (str(author))
            authorname = authstring[27:-5]
            if authorname in authunknowns:
                authdata = "Author: Unknown"
                textdata.append(authdata)
            elif authorname not in authunknowns:
                removables = ["[", "]", "\n"]
                for item in removables:
                    if item in authorname:
                        itemplace = authorname.find(item)
                        authorname = authorname[:itemplace] + authorname[itemplace + len(item):]
                authdata = "Author: " + authorname
                textdata.append(authdata)
        """Finds all languages in the text"""
        langtags = []
        for header in infohtml.findAll("h5"):
            headerstring = (str(header))
            """Finds Irish Language Information where identification conforms to expected format"""
            if "Language: [GA]" in headerstring:
                irishinfo = headerstring[19:-5]
                irishtypes = []
                if "Old" in irishinfo:
                    irishtypes.append("Old Irish")
                if "Middle" in irishinfo:
                    irishtypes.append("Middle Irish")
                emi_list = ["Early Modern", "Early modern", "(Early) Modern", "Early-Modern", "early Modern",
                            "Classical Modern"]
                for variant in emi_list:
                    if variant in irishinfo:
                        if "Early Modern Irish" not in irishtypes:
                            irishtypes.append("Early Modern Irish")
                if not irishtypes:
                    irishtypes.append("not specified")
                textdata.append("Form(s) of Irish: " + str(irishtypes))
                """Finds Irish Language Information where identification does not conform to expected format"""
            elif "Language: GA" in headerstring:
                infohtmlstring = (str(infohtml))
                headerpos = infohtmlstring.find(headerstring)
                headerlen = len(headerstring)
                headerend = headerpos + headerlen
                splitstring = infohtmlstring[headerend:]
                paraend = splitstring.find("</p>")
                teststring = splitstring[4:paraend]
                removables = ["\n"]
                for item in removables:
                    if item in teststring:
                        itemcount = teststring.count(item)
                        for i in range(0, itemcount):
                            spacepos = teststring.find(item)
                            teststring = teststring[:spacepos] + teststring[spacepos + len(item):]
                irishinfo = teststring
                irishtypes = []
                if "Old" in irishinfo:
                    irishtypes.append("Old Irish")
                if "Middle" in irishinfo:
                    irishtypes.append("Middle Irish")
                emi_list = ["Early Modern", "Early modern", "(Early) Modern", "Early-Modern", "early Modern",
                            "Classical Modern"]
                for variant in emi_list:
                    if variant in irishinfo:
                        if "Early Modern Irish" not in irishtypes:
                            irishtypes.append("Early Modern Irish")
                if not irishtypes:
                    irishtypes.append("not specified")
                textdata.append("Form(s) of Irish: " + str(irishtypes))
            elif "Language: [" in headerstring:
                langtag = headerstring[15:17]
                langtags.append(langtag)
            elif "Language: " in headerstring:
                langtag = headerstring[14:16]
                langtags.append(langtag)
        if langtags:
            textdata.append(langtags)
        elif not langtags:
            textdata.append("None")
        textsinfo.append(textdata)
        """Prints an error message if any base links are in an unexpected format"""
    if no_baselink:
        print("The following links are broken: " + str(no_baselink))
    return textsinfo


# testlist = textlinks('http://celt.ucc.ie/irlpage.html')
# for data in textinfo(testlist[0]):
#     print(data)
