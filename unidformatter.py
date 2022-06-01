def unid_formatter(unid_url):
    unid = unid_url.partition("unid=")[2]
    eight = unid[0:8]
    four1 = unid[8:12]
    four2 = unid[12:16]
    four3 = unid[16:20]
    twelve = unid[20:]
    delimiter = "-"
    formatted = (eight+delimiter+four1+delimiter+four2+delimiter+four3+delimiter+twelve)
    return formatted

print(unid_formatter("https://boskalis.support.topdesk.net/tas/secure/person?unid=4c1e84b4d658582cafaecdf8aa2f1af5"))

