import feedparser
from datetime import datetime
import time

def rss_reader(url):
    try:
        return feedparser.parse(url)["entries"][0]
    except:
        return

def clean(liste):
    stop = False
    word = ''
    for w in str(liste):
        if str(w) == '<':
            stop = True
        if stop == False:
            word = word+str(w)
        if str(w) == '>':
            stop = False
    return(word.replace("\n",""))

def get(conf):
    news_feeds = conf["secret"]["rss_feeds"].split()
    if len(news_feeds) = 0:
        return "Es ist kein RSS-Feed hinterlegt"
    title1 = list()
    title = list()
    description1 = list()
    description = list()
    heute = datetime.strptime(time.strftime("%d.%m.%Y %H:%M:%S"), "%d.%m.%Y %H:%M:%S")
    for news_feed in news_feeds:
        try:
            response = rss_reader(news_feed)
            date = datetime.fromtimestamp(time.mktime(response['published_parsed']))
            if (round((heute - date).seconds/3600, 0) <= 2):
                title1 += [response['title']]
                description1 += [response['description']]
        except:
            pass
    for i in description1:
        description += [clean(i)]
    for e in title1:
        title += [clean(e)]
    if len(title) > 2:
        rss_str = ""
        for item in title:
            rss_str += str(item) + ', <break time="100ms"/>'
        return "{} und {}.".format(rss_str, title[-1])
    elif len(title) == 1:
        return "{}. {}".format(title[0], description[0])
    elif len(title) == 2:
        return "{},<break time='100ms'/> {}".format(title[0], title[1])
    else:
        return "Es gibt keine News."
