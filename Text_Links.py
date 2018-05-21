"""Finds all hyperlinks on main Irish page of CELT.
   Separates Irish texts from translations and non-text links."""


from Findrefs import findrefs
from Combine_Link import combinelink


def textlinks(url):
    brokencount = 0
    gaelcount = 0
    transcount = 0
    ntcount = 0
    ga_links = []
    eng_links = []
    fr_links = []
    otherlinks = []
    """opens all links on irish text page"""
    for ref in findrefs(url):
        # print(ref)
        text_type = ["published/G", "published/T", "published/F"]
        fixedlinks = []
        """counts broken links found"""
        if ref == "":
            brokencount += 1
            # print(brokencount)
        if ref[0:11] in text_type:
            """finds and counts working links to Irish texts"""
            if ref[0:11] == text_type[0]:
                gaelcount += 1
                g_link = combinelink(url, ref)
                ga_links.append(g_link)
                # print(str(gaelcount) + ": " + g_link)
                """finds and counts working links to English translations of Irish texts"""
            elif ref[0:11] == text_type[1]:
                transcount += 1
                t_link = combinelink(url, ref)
                eng_links.append(t_link)
                # print(str(transcount) + ": " + t_link)
                """finds and counts working links to French translations of Irish texts"""
            elif ref[0:11] == text_type[2]:
                transcount += 1
                t_link = combinelink(url, ref)
                fr_links.append(t_link)
                # print(str(transcount) + ": " + t_link)
        elif ref[:4] == "http":
            ntcount += 1
            other_link = ref
            otherlinks.append(other_link)
            # print(str(ntcount) + ": " + other_link)
        else:
            ntcount += 1
            other_link = combinelink(url, ref)
            otherlinks.append(other_link)
            # print(str(ntcount) + ": " + other_link)
    alllinks = [ga_links, eng_links, fr_links, otherlinks]
    return alllinks


# lists = textlinks('http://celt.ucc.ie/irlpage.html')
# for list in lists:
#     for link in list:
#         print(link)
