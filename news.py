import feedparser
from datetime import date,datetime
import time
def rss_reader(url,art):
    try:
        return(feedparser.parse(url)["entries"][0][art])
    except:
        return()
def clean(list):
    stop = False
    word = ''
    for w in str(list):
        if str(w) == '<':
            stop = True
        if stop == False:
            word = word+str(w)
        if str(w) == '>':
            stop = False
    return(word.replace("\n",""))
def postillion():
    liste = ["https://tagesschau.de/xml/rss2","https://www.transfermarkt.de/rss/news"]
    title1 = []
    title = []
    description1 = []
    description = []
    heute = datetime.strptime(time.strftime("%d.%m.%Y %H:%M:%S"), "%d.%m.%Y %H:%M:%S")
    for datei in liste:
            try:
                date = datetime.fromtimestamp(time.mktime(rss_reader(datei, 'published_parsed')))
                if (round((heute - date).seconds/3600, 0) <= 2):
                    title1 += [rss_reader(datei, 'title')]
                    description1 += [rss_reader(datei, 'description')]
            except:
                None
    for i in description1:
        description += [clean(i)]
    for e in title1:
        title += [clean(e)]
    if len(title) > 1:
        rss_str = ""
        for item in title:
            rss_str = rss_str+str(item)+', '
        return("{} und {}.".format(rss_str,title[-1]))
    elif len(title) == 1:
        return("{}. {}".format(title[0],description[0]))
    else:
        return("Es gibt keine News.")